import requests
import json
import re

# Example usage
data = {
    "Transaction ID": "TXN-2023-5ABD",
    "Extracted Entity": ["Wells Fargo", "Global FinTech Corp"],
    "Entity Type": ["Corporation", "Corporation"],
    "News API": [
        {"Entity": "Wells Fargo", "Risk Score": 0.4, "Confidence Score": 0.6, "Reason": "https://news.example.com/wells-fargo"},
        {"Entity": "Global FinTech Corp", "Risk Score": 0.3, "Confidence Score": 0.7, "Reason": "https://news.example.com/global-fintech"}
    ],
    "Edgar API": [
        {"Entity": "Wells Fargo", "Risk Score": 0.35, "Confidence Score": 0.65, "Reason": "SEC Filing XYZ"},
        {"Entity": "Global FinTech Corp", "Risk Score": 0.25, "Confidence Score": 0.75, "Reason": "SEC Filing ABC"}
    ]
}

def generate_risk_assessment(data):
    GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"

    api_key = "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"
    
    # Define the headers
    HEADERS = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    # Define the prompt template
    PROMPT_TEMPLATE = """
    You are an AI model designed for financial risk assessment. Given a transaction containing extracted entities 
    and their associated risk scores from multiple sources (News API, SEC EDGAR), along with your base trained knowledge, 
    your task is to generate a structured JSON response evaluating the risk.

    Instructions:
    - Maintain the same Transaction ID, Extracted Entity, and Entity Type from the input.
    - Combine multiple risk scores from News API, SEC EDGAR, and your base trained knowledge using a weighted average approach to evaluate the final risk score.
    - Extract supporting evidence for the risk score from news reports, filings, and your trained base intelligence.
    - Clearly justify the reason for risk classification, including any specific red flags, past regulatory actions, or controversies.
    - Include citation links from the News API's reason key in the final JSON response.
    - Using the combined knowledge update the 'Supporting Evidence' field combining all the information from all the sources.
    - **Respond strictly in a valid JSON format with no extra text or explanations. Do not include markdown formatting (e.g., ```json).**
    - In the response, dont include "Here is the generated JSON response:", or any other description apart from the json

    Input JSON:
    {input_data}

    Expected JSON Output Response Format:
    {{
      "Transaction ID": "{transaction_id}",
      "Extracted Entity": {extracted_entity},
      "Entity Type": {entity_type},
      "Risk Score": ,
      "Confidence Score": ,
      "Supporting Evidence": ["Google news", "Edgar", "LLM Knowledge"],
      "Reason": {{
        "entity1": "Explanation with risk score - source link",
        "entity2": "Explanation with risk score - source link"
      }}
    }}
    Now, generate the JSON response strictly following the format above.
    """
    
    # Format the prompt with input data
    formatted_prompt = PROMPT_TEMPLATE.format(
        input_data=json.dumps(data), # Removed indent=2 to avoid extra newline and whitespace
        transaction_id=data['Transaction ID'],
        extracted_entity=data['Extracted Entity'],
        entity_type=data['Entity Type']
    )
    
    # Define the request payload
    PAYLOAD = {
        "model": "llama3-8b-8192",  # or "mixtral-8x7b-32768" based on your preference
        "messages": [
            {"role": "system", "content": "You are a financial risk analysis expert."},
            {"role": "user", "content": formatted_prompt}
        ],
        "temperature": 0.3
    }
    
    # Make the API call
    response = requests.post(GROQ_URL, headers=HEADERS, json=PAYLOAD)
    
    if response.status_code == 200:
      return json.loads(response.json()['choices'][0]['message']['content'])
    else:
        return {"error": f"Error {response.status_code}: {response.text}"}