from transformers import AutoTokenizer, AutoModelForSequenceClassification
import requests
import pandas as pd
from io import StringIO
import re
import torch
import torch.nn.functional as F
import numpy as np
import json


model_name = "nlpaueb/legal-bert-small-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=2)

HIGH_RISK_KEYWORDS = [
    "fraud", "money laundering", "sanction", "blacklist", "terrorist", "corruption",
    "illegal", "bribery", "scam", "ponzi scheme", "crime", "penalty", "regulatory fine"
]

OFAC_SDN_CSV_URL = "https://www.treasury.gov/ofac/downloads/sdn.csv"

def fetch_ofac_us_list():
    response = requests.get(OFAC_SDN_CSV_URL)
    if response.status_code == 200:
        data = response.content.decode('utf-8')
        df = pd.read_csv(StringIO(data), header=None, dtype=str)
        print("OFAC SDN List Fetched Successfully!")
        df = df[[0, 1, 2, 3, 11]]
        df.columns = ["ID", "Name", "Type", "Program", "Info"]
        return df
    else:
        print("Failed to fetch OFAC data.")
        return None

def check_sanctions(entity_name, df):
    df = df.fillna("N/A")
    match = df[df["Name"].str.fullmatch(entity_name, case=False, na=False)]

    if not match.empty:
        return {
            "Sanctioned": True,
            "Programs": match["Program"].values.tolist(),
            "Entity Type": match["Type"].values.tolist(),
            "Info": match["Info"].values.tolist()
        }
    else:
        return {"Sanctioned": False, "Programs": None, "Entity Type": None, "Info": None}

def compute_risk_score(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    logits = outputs.logits 
    num_classes = logits.shape[1]
    if num_classes == 3:
        probabilities = F.softmax(logits, dim=-1)
        sentiment_risk = probabilities[0][0].item()
    else:
        sentiment_risk = torch.max(F.softmax(logits, dim=-1)).item()
    keyword_risk = sum(bool(re.search(rf"\b{k}\b", text, re.IGNORECASE)) for k in HIGH_RISK_KEYWORDS)
    risk_score = round(min(1.0, sentiment_risk + (keyword_risk * 0.1)), 4)

    return risk_score

def score_US_Ofac(programs, info):
  sanctions_list = ["SDN", "CAPTA", "IRAN", "CUBA", "NORTH KOREA", "RUSSIA", "SYRIA", "VENEZUELA", "WMD", "NARCOTICS"]
  pattern = re.compile(r'\b(' + '|'.join(re.escape(term) for term in sanctions_list) + r')\b', re.IGNORECASE)
  score = 8
  if bool(pattern.search(" ".join(programs))):
    score += 1
  score += round(compute_risk_score(" ".join(info)),4)
  print(score)
  return score

def check_ofac_us(entities: list,text: str):
  """
  Check entities against the OFAC US sanctions list.
  This is a placeholder function. Replace with actual OFAC US checking logic.
  """
  ofac_us_df = fetch_ofac_us_list()
  risk_score = []
  sanctioned_entity = []
  if ofac_us_df is not None:
    for entity in entities:
      result = check_sanctions(entity['word'], ofac_us_df)
      if result["Sanctioned"]:
        sanctioned_entity.append(entity['word'])
        risk_score.append(score_US_Ofac(result['Programs'],result['Info']))
  if sanctioned_entity:
    data = {
      "Transaction ID": re.search(r'Transaction ID:\s*([A-Z0-9-]+)', text).group(1),
      "Extracted Entity": [entity['word'] for entity in entities],
      "Entity Type": ["Corporation" if item['entity_group'] == "ORG" else "Individual" for item in entities],
      "Risk Score": round(float(np.mean(risk_score))/10,4),
      "Supporting Evidence":["OFAC US Sanctions"],
      "Confidence Score": min(0.98, round(float(np.mean(risk_score))/10,4)+0.093),
      "Reason": (f"The following entities have been identified in the OFAC US sanctions list: {sanctioned_entity}. "
        f"Engaging with sanctioned entities poses regulatory, financial, and reputational risks.")
      }
    # json_output = json.dumps(data, indent=4, separators=(", ", ": "), ensure_ascii=False)
    return data
  return None