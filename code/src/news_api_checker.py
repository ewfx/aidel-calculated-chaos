import requests
from bs4 import BeautifulSoup
from transformers import pipeline
import re
import numpy as np

# Load the zero-shot classification model
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

# Define risk labels
RISK_LABELS = ["financial fraud", "corruption", "money laundering", "regulatory violation", "bribery", "tax evasion", "market manipulation", "sanctions violation", "safe"]

def fetch_news(entity_name, max_articles=5):
    """Fetch all news from Google News RSS for the given entity."""
    search_url = f"https://news.google.com/rss/search?q={entity_name}"
    response = requests.get(search_url)
    news_articles = []

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "xml")
        for item in soup.find_all("item")[:max_articles]:  # Limit the number of articles
            news_articles.append({
                "title": item.title.text,
                "link": item.link.text,
                "description": item.description.text
            })
    return news_articles

def analyze_risk(news_texts):
    """Analyze the risk level of a batch of news articles."""
    results = classifier(news_texts, RISK_LABELS)
    risks = []

    for result in results:
        highest_risk_label = result["labels"][0]
        highest_risk_score = result["scores"][0]
        risks.append({"label": highest_risk_label, "score": highest_risk_score})

    return risks

def check_news_api(entities, text):
    """Fetch news, analyze risk, and determine the highest risk score among all entities."""
    print("Checking news API for risk analysis...")
    highest_risk_score = 0
    risk_reasons = []

    for entity in entities:
        entity_name = entity['word']
        news_articles = fetch_news(entity_name)

        # Combine titles and descriptions for batch processing
        news_texts = [article["title"] + " " + article["description"] for article in news_articles]
        risk_results = analyze_risk(news_texts)

        for i, risk_result in enumerate(risk_results):
            if risk_result["label"] != "safe":
                if risk_result["score"] > highest_risk_score:
                    highest_risk_score = risk_result["score"]
                    risk_reasons = [f"{entity_name}: {risk_result['label']} ({risk_result['score']:.2f}) - {news_articles[i]['link']}"]

    confidence_score = min(1.0, highest_risk_score + 0.1)

    if highest_risk_score == 0:
        return None  # No risk detected, return null

    return {
        "Transaction ID": re.search(r'Transaction ID:\s*([A-Z0-9-]+)', text).group(1),
        "Extracted Entity": [entity['word'] for entity in entities],
        "Entity Type": ["Corporation" if item['entity_group'] == "ORG" else "Individual" for item in entities],
        "Risk Score": round(float(np.mean(highest_risk_score))/10,4),
        "Supporting Evidence": ["Google News"],
        "Confidence Score": round(float(np.mean(confidence_score))/10,4),
        "Reason": "; ".join(risk_reasons)
    }
    
if __name__ == "__main__":
    text = """
    Transaction ID: TXN-2023-5ABD
    Sender:
    - Name: "Horizons consulting LLC"
    - Account: IBAN CN56 0482 6781 9898 (Swiss Bank)
    - Address: Due du marche 12, Geneva, Switzerland
    - Notes: Consulting fees for project Aurora
    Receiver:
    - Name: "BOSCO GILAN"
    - Account: IBAN AQ45 6781 0865 (Cayman National Bank, KY)
    - Address: Due du marche 12, George town, Cayman Islands
    - Notes: Consulting fees for project Aurora
    Transaction Type: Wire transfer
    Reference: Charitable donation
    Additional notes:
    Urgent transaction authorized by Mr. Ali Al-Mansoori (Director) and MUNITIONS INDUSTRY DEPARTMENT.
    Funds were transferred via Quantum Holding Ltd. and Global FinTech Corp. Exit node was Switzerland.
    Approved by CEO Richard Branson at Amazon Inc.
    """

    entities = [
        {'entity_group': 'PER', 'score': np.float32(0.99998856), 'word': 'Wells Fargo', 'start': 702, 'end': 717},
        {'entity_group': 'ORG', 'score': np.float32(0.9999887), 'word': 'Amazon Inc', 'start': 721, 'end': 731}
    ]

    print(check_news_api(entities, text))