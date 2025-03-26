from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline
import requests
import pandas as pd
from io import StringIO
import re
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import torch.nn.functional as F
import os
import numpy as np
import json
import xml.etree.ElementTree as ET

UN_SANCTIONS_URL = "https://scsanctions.un.org/resources/xml/en/consolidated.xml"

classifier = pipeline("text-classification", model="ProsusAI/finbert")

def fetch_ofac_un_list():
  response = requests.get(UN_SANCTIONS_URL)
  if response.status_code == 200:
    root = ET.fromstring(response.content)
    return root
  else:
    print("Failed to fetch OFAC data.")
    return None

def get_risk_score_un(sanction_reason, country):
    input_text = f"Sanctioned entity due to {sanction_reason} in {country}."
    result = classifier(input_text)[0]
    label_to_risk = {"positive": 0.7, "neutral": 0.8, "negative": 0.9}
    risk_score = label_to_risk.get(result["label"].lower(), 0.5)  # Default to neutral risk
    return risk_score

def compute_risk_score_un(entity, root):
    entity_name = entity['word']
    if entity['entity_group'] == "PER":
        for person in root.findall(".//INDIVIDUALS/INDIVIDUAL"):
            full_name = " ".join(filter(None, [person.findtext("FIRST_NAME"), person.findtext("SECOND_NAME")]))
            if entity_name.lower() in full_name.lower():
                risk_score = get_risk_score_un(person.findtext("COMMENTS1"), person.findtext("INDIVIDUAL_PLACE_OF_BIRTH/PLACE_COUNTRY"))
                return risk_score
    elif entity['entity_group'] == "ORG":
        for entity in root.findall(".//ENTITIES/ENTITY"):
            name = entity.findtext("FIRST_NAME")
            if entity_name.lower() in name.lower():
                risk_score = get_risk_score_un(entity.findtext("COMMENTS1"), entity.findtext("ENTITY_ADDRESS/COUNTRY"))  # FIXED
                return risk_score
    return 0



def check_ofac_un(entities: list, transaction: str):
    """
    Check entities against the OFAC UN sanctions list.
    This is a placeholder function. Replace with actual OFAC UN checking logic.
    """
    ofac_un_root = fetch_ofac_un_list()
    risk_score = []
    sanctioned_entity = []
    if ofac_un_root is not None:
      for entity in entities:
        score = compute_risk_score_un(entity,ofac_un_root)
        if score > 0:
          risk_score.append(score)
          sanctioned_entity.append(entity['word'])
    if sanctioned_entity:
      data = {
        "Transaction ID": re.search(r'Transaction ID:\s*([A-Z0-9-]+)', transaction).group(1),
        "Extracted Entity": [entity['word'] for entity in entities],
        "Entity Type": ["Corporation" if item['entity_group'] == "ORG" else "Individual" for item in entities],
        "Risk Score": round(float(np.mean(risk_score)),4),
        "Supporting Evidence":["OFAC UN Sanctions"],
        "Confidence Score": min(0.95, round(float(np.mean(risk_score)),4)+0.091),
        "Reason": (f"The following entities have been identified in the OFAC UN sanctions list: {sanctioned_entity}. "
        f"Engaging with sanctioned entities poses regulatory, financial, and reputational risks.")
      }
      print(data)
      return data
    return None
