# 🚀 Risk Analysis Workflow with Gen AI-driven Entity Intelligence

## 📌 Table of Contents
- [Introduction](#introduction)
- [Demo](#demo)
- [Inspiration](#inspiration)
- [What It Does](#what-it-does)
- [How We Built It](#how-we-built-it)
- [Challenges We Faced](#challenges-we-faced)
- [How to Run](#how-to-run)
- [Tech Stack](#tech-stack)
- [Team](#team)

---

## 🎯 Introduction
This project focuses on Gen AI-driven risk analysis for financial transactions. It processes payment transactions, extracts entities, checks for sanctions, analyzes news and financial filings, and evaluates risk using an AI-powered approach. The goal is to enhance compliance monitoring and financial risk detection.

## 🎥 Demo
🔗 [Live Demo](#) (if applicable)  
📹 [Video Demo](#) (if applicable)  
🖼️ Screenshots:

![Screenshot 1](link-to-image)

## 💡 Inspiration
The project was inspired by the increasing need for **automated risk assessment** in financial transactions. Many organizations struggle with detecting high-risk entities manually, leading to compliance violations. This system automates the screening process using AI and regulatory data.

## ⚙️ What It Does
1. **Extracts Entities:** Identifies companies, persons, and financial institutions from transaction data.
2. **OFAC & UN Sanctions Check:** Flags entities present in global sanctions lists.
3. **News Risk Analysis:** Fetches news articles and classifies their risk level using NLP models.
4. **SEC Edgar Analysis:** Retrieves financial filings to detect anomalies.
5. **AI-powered Risk Assessment:** Uses the Llama 3 8B model for final risk classification.
6. **User-friendly UI:** Provides insights and justifications for flagged transactions.

## 🛠️ How We Built It
- **Streamlit UI:** Allows users to upload transaction files and view results.
- **FastAPI Backend:** Processes transaction data and interacts with AI models.
- **BERT-based Classifier:** Assesses risk in news articles.
- **SEC Edgar API:** Retrieves regulatory filings for risk evaluation.
- **Llama 3 8B Model:** Aggregates insights to assign a final risk classification.

## 🚧 Challenges We Faced
- **Entity Extraction Complexity:** Handling unstructured transaction formats.
- **Sanctions List Updates:** Ensuring real-time accuracy in screening.
- **Financial Document Parsing:** Processing and interpreting SEC filings efficiently.
- **LLM Computation Overhead:** Optimizing model inference for real-time decision-making.

## 🏃 How to Run
1. Clone the repository  
   ```sh
   git clone https://github.com/your-repo.git
   ```
2. Install dependencies  
   ```sh
   pip install -r requirements.txt  
   ```
3. Run the project  
   ```sh
   streamlit run app.py  
   ```

## 🏗️ Tech Stack
- **Frontend:** Streamlit
- **Backend:** FastAPI
- **Database:** PostgreSQL
- **NLP Models:** BERT, OpenAI API
- **Financial APIs:** SEC Edgar
- **LLM:** Llama 3 8B Model

## 👥 Team
- **Vinay Pandey** 
- **S. Rohith**
- **Vishal Ramesh K**
- **Keerthana Sureshkumar**

## 🎯 Conclusion
This AI-powered risk analysis system enhances financial compliance by automating entity screening, risk assessment, and regulatory checks. By leveraging LLMs, NLP models, and financial data sources, it ensures accurate and transparent decision-making in financial transactions.
