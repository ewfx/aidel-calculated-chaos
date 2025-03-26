import json
import os
import threading
import re
from threading import Thread

import requests
import streamlit as st
import uvicorn
from fastapi import FastAPI, File, UploadFile
from pyngrok import ngrok
import time

from entity_extractor import extract_entities
from news_api_checker import check_news_api
from ofac_un_checker import check_ofac_un
from ofac_us_checker import check_ofac_us
from sec_edgar_checker import check_sec_edgar
from wikidata_checker import check_wikidata
from llm_analyzer import generate_risk_assessment

# FastAPI backend
app = FastAPI()

# Function to process the .txt file
def process_transactions(file_content: str):
    normalized_content = file_content.replace("\r\n", "")
    transactions = normalized_content.split("---")
    transactions_list = [t.strip() for t in transactions if t.strip()]
    results = []

    for txn in transactions_list:
        # Extract entities for the transaction
        entities = extract_entities(txn)
        
        # Check entities against OFAC US list
        ofac_us_results = check_ofac_us(entities, txn)
        if ofac_us_results:  
            results.append(ofac_us_results)
            continue  
        
        # Check entities against OFAC UN list
        ofac_un_results = check_ofac_un(entities, txn)
        if ofac_un_results:  
            results.append(ofac_un_results)
            continue  
        
         # Check entities against News API
        news_results = check_news_api(entities, txn)
        news_data_llm = []
        if news_results["Risk Score"] > 0.8:
            results.append(news_results)
            continue
        else:
            news_data_llm.append({
                "Risk Score": news_results["Risk Score"],
                "Reason": news_results["Reason"]
            })

        
        # Check entities against SEC Edgar API
        sec_edgar_results = check_sec_edgar(entities, txn)
        sec_edgar_data_llm = []
        if sec_edgar_results["Risk Score"] > 0.8:  
            results.append(sec_edgar_results)
            continue 
        else:
            sec_edgar_data_llm.append({
                "Risk Score": sec_edgar_results["Risk Score"],
                "Reason": sec_edgar_results["Reason"]
            })
        
        # Check entities against Wikidata
        # wikidata_results = check_wikidata(entities)
        # if wikidata_results:
        #     results.append(wikidata_results)
        #     continue
        
        llm_data = {
            "Transaction ID": re.search(r'Transaction ID:\s*([\w-]+)', txn).group(1),
            "Extracted Entity": [entity['word'] for entity in entities],
            "Entity Type": ["Corporation" if item['entity_group'] == "ORG" else "Individual" for item in entities],
            "News API": news_data_llm,
            "Edgar API": sec_edgar_data_llm
            }
        
            
        llm_response = generate_risk_assessment(llm_data)
        results.append(llm_response)
    
    
    return results

# FastAPI route to handle file uploads
@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    content = await file.read()
    decoded_content = content.decode("utf-8")
    result = process_transactions(decoded_content)
    print(result,type(result))
    return {"transactions": result}

# Run FastAPI in a separate thread
def run_fastapi():
    uvicorn.run(app, host="0.0.0.0", port=8000)

threading.Thread(target=run_fastapi, daemon=True).start()

# Set page config for better UI
st.set_page_config(
    page_title="Payment Transaction Entity Risk Analyzer",
    page_icon="💳",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown(
    """
    <style>
    .main-title { font-size: 50px; text-align: center; color: #4A90E2; font-weight: bold; }
    .sub-text { text-align: center; color: #555; font-size: 16px; }
    .upload-box { border: 2px dashed #4A90E2; padding: 20px; border-radius: 10px; text-align: center; }
    .success-box { background-color: #E6F7E6; padding: 10px; border-radius: 5px; color: #008000; font-weight: bold; }
    .error-box { background-color: #FDEDEC; padding: 10px; border-radius: 5px; color: #B22222; font-weight: bold; }
    .stTextArea>label { font-size: 14px; font-weight: bold; }
    </style>
    """,
    unsafe_allow_html=True
)

# UI Header
st.markdown("<p class='main-title'>🔍 Payment Transaction Entity Risk Analyzer</p>", unsafe_allow_html=True)
st.write("---")

# Sidebar with extra info
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3144/3144456.png", width=100)
st.sidebar.title("⚡ Features")
st.sidebar.markdown(
    """
    - ✅ Extracts entities from transactions  
    - ✅ Checks against OFAC US sanction lists  
    - ✅ Checks against OFAC UN sanction lists  
    - ✅ Verifies against news sources  
    - ✅ Queries SEC Edgar API for validation 
    - ✅ Runs risk analysis using an LLM   
    """
)

# File upload section
st.markdown("<div class='upload-box'>📂 Upload Payment Transactions `.txt` file for entity screening and risk analysis</div>", unsafe_allow_html=True)
uploaded_file = st.file_uploader("Choose a file", type=["txt"])

if uploaded_file is not None:
    with st.spinner("Processing file... ⏳"):
        # Read file content
        content = uploaded_file.read().decode("utf-8")
        
        # Reset the file pointer to the beginning after reading
        uploaded_file.seek(0)

        # Create a placeholder for the checklist
        checklist_placeholder = st.empty()

        # Simulate processing steps with a checklist
        checklist = [
            "Extracts entities from transactions",
            "Checks against OFAC US sanction lists",
            "Checks against OFAC UN sanction lists",
            "Verifies against news sources",
            "Queries SEC Edgar API for validation",
            "Runs risk analysis using an LLM"
        ]

        # Display the checklist dynamically
        for i, step in enumerate(checklist):
            checklist_placeholder.markdown(
                f"""
                <ul>
                    {''.join([f"<li>{'✅' if j <= i else '⏳'} {checklist[j]}</li>" for j in range(len(checklist))])}
                </ul>
                """,
                unsafe_allow_html=True
            )
            # Simulate processing time for each step
            if step == "Runs risk analysis using an LLM":
                time.sleep(3)  # LLM takes the most time
            else:
                time.sleep(1)

        # Send request to FastAPI backend
        response = requests.post(
            "http://127.0.0.1:8000/upload/",
            files={"file": (uploaded_file.name, uploaded_file, uploaded_file.type)}
        )
        
        if response.status_code == 200:
            st.success("✅ File uploaded successfully!")
            st.text_area("📄 File Content Preview", content, height=200)

            # Parse the response JSON
            response_data = response.json()
            transactions = response_data.get("transactions", [])

            # Display results in a fancy UI
            if transactions:
                st.markdown("<h3 style='text-align: center; color: #4A90E2;'>🛡️ Risk Assessment Results</h3>", unsafe_allow_html=True)
                for idx, transaction in enumerate(transactions, start=1):
                    st.markdown(f"<div class='success-box'>🔹 <b>Transaction {idx}</b></div>", unsafe_allow_html=True)
                    st.json(transaction)  # Display transaction details in JSON format
            else:
                st.markdown("<div class='error-box'>⚠️ No transactions found in the response!</div>", unsafe_allow_html=True)
        else:
            st.markdown("<div class='error-box'>❌ Error processing file! Please try again.</div>", unsafe_allow_html=True)

st.write("---")
st.info("📌 **Note:** Large files may take longer to process. Please be patient.")