# README: Risk Analysis Workflow with AI-driven Entity Intelligence

## Overview
This document explains the sequential workflow diagram. The system is designed to process payment transactions, extract entities, check for sanctions, analyze news and financial filings, and evaluate risk using an AI-driven approach. The workflow involves multiple components such as Streamlit UI, FastAPI, entity extraction, OFAC screening, news APIs, SEC Edgar filings, and an LLM (Llama 3 8B model) for risk assessment.

---

## Workflow Breakdown

### **1. Streamlit UI**
- **Input:** A `.txt` file containing financial transactions.
- **Action:** The user uploads the transaction file via a Streamlit interface.
- **Dispatch:** The file is sent to the FastAPI endpoint for processing.

### **2. FastAPI Endpoint for File Reception**
- **Input:** The uploaded `.txt` file.
- **Action:** The file is parsed, and entities (such as companies, persons, and financial institutions) are extracted.
- **Output:** A structured list of transactions with detected entities.
- **Dispatch:** The extracted entities are sent to the entity extraction module.

### **3. Entity Extraction Module**
- **Input:** The structured transactions with entities.
- **Action:** Identifies and extracts relevant entities from the transactions.
- **Output:** A list of entities involved in the transactions.
- **Dispatch:** The entity list is sent to the OFAC screening module for compliance checks.

### **4. OFAC Controller**
- **Input:** List of extracted entities.
- **Action:** Checks if any entity is flagged under OFAC (Office of Foreign Assets Control) sanctions lists.
- **Databases Queried:**
  - OFAC US List
  - OFAC UN List
  - PEPs (Politically Exposed Persons) and shell company databases.
- **Output:** Entities classified based on their presence in these lists along with associated risk metrics.
- **Dispatch:** The flagged entity list is sent to the News API Controller for further risk validation.

### **5. News API Controller**
- **Input:** Entity objects with OFAC response.
- **Action:**
  - Fetches news articles related to flagged entities from sources such as Google News, Wikipedia, Reuters.
  - Uses a **BERT-based classifier** to assess the risk level of the news articles (e.g., financial fraud, regulatory violations, corruption, etc.).
- **Output:** Risk metrics calculated based on news content.
- **Dispatch:** The classified news articles and their risk scores are sent to the SEC Edgar Controller.

### **6. SEC Edgar Controller**
- **Input:** News responses with flagged entity objects.
- **Action:**
  - Fetches SEC Edgar filings related to the entity.
  - Identifies anomalies in financial statements, regulatory violations, and reported risks.
- **Output:** SEC Edgar anomalies and financial risk observations.
- **Dispatch:** The financial risk observations are sent to the Llama 3 LLM Model.

### **7. Llama 3 8B LLM Model**
- **Input:**
  - News API risk assessments.
  - SEC Edgar filing anomalies.
  - Previous observations and stored knowledge.
- **Action:**
  - Uses a **Retrieval-Augmented Generation (RAG) mechanism** to extract insights from financial data.
  - Provides a comprehensive risk score based on compiled data sources.
- **Output:** A final risk classification for each entity with detailed justification.
- **Return:** The final risk classification is sent back to the Streamlit UI.

### **8. Streamlit UI (Final Output)**
- **Input:** Risk classification and details from the LLM model.
- **Output:**
  - Displays a summary of flagged transactions with risk scores.
  - Highlights entities with "Extremely High Risk" classifications.
  - Provides links to supporting news articles and SEC filings for transparency.

---

## Summary of Risk Calculation
1. **OFAC List Check:** Determines if the entity is on the US or UN sanctions lists.
2. **News API Classification:** Identifies negative media coverage using NLP-based classification.
3. **SEC Edgar Analysis:** Detects financial anomalies and compliance issues.
4. **LLM-based Evaluation:** Aggregates all insights and assigns a final risk classification.

---

## Technologies Used
- **Streamlit:** UI for uploading transaction files and displaying results.
- **FastAPI:** Backend API for processing transactions.
- **BERT-based Classifier:** Used to assess news article risk.
- **SEC Edgar API:** Fetches financial regulatory filings.
- **Llama 3 8B Model:** Pretrained financial AI model for risk assessment.
- **OFAC/UN Sanctions Database:** Identifies high-risk entities.

---

## Conclusion
This system provides an AI-powered approach to **automated financial entity risk assessment**, integrating multiple data sources to provide comprehensive risk analysis. By leveraging NLP, financial anomaly detection, and LLM-based reasoning, the model ensures accurate and transparent decision-making in financial compliance monitoring.
