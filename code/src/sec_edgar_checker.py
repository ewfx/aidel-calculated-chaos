import requests
import re
from transformers import pipeline

# Define high-risk filings and their reasons
HIGH_RISK_FILINGS = {
    "8-K": "Reports material events like lawsuits, fraud investigations, or executive resignations.",
    "144": "Indicates insider stock sales, which may suggest lack of confidence in the company.",
    "4": "Discloses insider trading, which could indicate undisclosed risks or potential misconduct."
}

# High-risk jurisdictions (offshore tax havens or sanctioned regions)
HIGH_RISK_JURISDICTIONS = {"Cayman Islands", "Panama", "Russia", "North Korea", "Iran"}

# Load a transformer-based classifier for textual risk analysis
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def get_cik(entity_name):
    """Fetches CIK (Central Index Key) for a given company."""
    search_url = "https://efts.sec.gov/LATEST/search-index"
    headers = {"User-Agent": "SEC-Filing-Analyzer/1.0 (contact@yourdomain.com)"}

    response = requests.get(search_url, params={"keysTyped": entity_name, "category": "company"}, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if "hits" in data and len(data["hits"]["hits"]) > 0:
            return data["hits"]["hits"][0]["_id"].zfill(10)  # Ensure CIK is 10 digits
    return None

def fetch_sec_data(cik):
    """Fetches SEC filings for a given CIK."""
    base_url = f"https://data.sec.gov/submissions/CIK{cik}.json"
    headers = {"User-Agent": "SEC-Filing-Analyzer/1.0 (contact@yourdomain.com)"}

    response = requests.get(base_url, headers=headers)
    return response.json() if response.status_code == 200 else {"error": "Failed to fetch SEC data"}

def analyze_filing_text(filing_text):
    """Classifies filing text for risk assessment using a transformer model."""
    labels = ["fraud", "regulatory violation", "lawsuit", "safe"]
    result = classifier(filing_text, labels)

    highest_risk_label = result["labels"][0]
    highest_risk_score = result["scores"][0]

    if highest_risk_label != "safe":
        return highest_risk_score, f"SEC filing text suggests possible {highest_risk_label} (Confidence: {highest_risk_score:.2f})"
    return 0, None

def check_sec_edgar(entities: list, transaction: str):
    """Analyzes SEC filings, assigns a normalized risk score (0-1), and provides explanations."""
    total_risk_score = 0
    total_confidence_score = 0
    risk_reasons = []
    max_possible_risk = len(entities) * 5  # Max risk based on 5 filings per entity

    for entity in entities:
        entity_name = entity['word']
        cik = get_cik(entity_name)
        if not cik:
            risk_reasons.append(f"No SEC records found for {entity_name}.")
            continue

        sec_data = fetch_sec_data(cik)
        jurisdiction = sec_data.get("stateOfIncorporation", "Unknown")
        recent_filings = sec_data.get("filings", {}).get("recent", {})
        forms = recent_filings.get("form", [])
        filing_dates = recent_filings.get("filed", [])
        filing_texts = recent_filings.get("text", [])  # Assuming we can fetch filing texts

        for i, form_type in enumerate(forms[:5]):  # Analyze last 5 filings
            if form_type in HIGH_RISK_FILINGS:
                reason = HIGH_RISK_FILINGS[form_type]
                
                # Ensure we do not access out-of-range indexes
                filing_date = filing_dates[i] if i < len(filing_dates) else "Unknown Date"
                
                risk_reasons.append(f"{entity_name} filed {form_type} on {filing_date}: {reason}")
                total_risk_score += 1  # Increase risk score

                # Analyze filing text for deeper insights
                if i < len(filing_texts) and filing_texts[i]:  
                    text_risk_score, text_risk_reason = analyze_filing_text(filing_texts[i])
                    if text_risk_reason:
                        risk_reasons.append(f"{entity_name}: {text_risk_reason}")
                        total_risk_score += text_risk_score  # Increase risk based on NLP

        # Jurisdiction check
        if jurisdiction in HIGH_RISK_JURISDICTIONS:
            risk_reasons.append(f"{entity_name} is incorporated in {jurisdiction}, a high-risk jurisdiction.")
            total_risk_score += 2  # Higher weight for offshore risk

    # Normalize risk score (0 to 1)
    final_risk_score = min(total_risk_score / max_possible_risk, 1.0) if max_possible_risk > 0 else 0
    confidence_score = min(1.0, final_risk_score+0.09)

    transaction_id_match = re.search(r'Transaction ID:\s*([A-Z0-9-]+)', transaction)
    transaction_id = transaction_id_match.group(1) if transaction_id_match else "Unknown"

    data = {
        "Transaction ID": transaction_id,
        "Extracted Entity": [entity['word'] for entity in entities],
        "Entity Type": ["Corporation" if item['entity_group'] == "ORG" else "Individual" for item in entities],
        "Risk Score": round(final_risk_score, 2),
        "Supporting Evidence": ["SEC EDGAR Filing"],
        "Confidence Score": round(confidence_score, 2),
        "Reason": " | ".join(risk_reasons) if risk_reasons else "No significant risks detected."
    }

    return data
