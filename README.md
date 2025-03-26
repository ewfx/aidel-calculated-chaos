# 🚀 Risk Analysis Workflow with Gen AI-driven Entity Intelligence

## 📌 Table of Contents
- [Introduction](Introduction)
- [Demo](https://drive.google.com/file/d/1zfLjbGGiQM5OJMs8UFQ7v0u38tvk6duo/view?usp=sharing )
- [Inspiration](#inspiration)
- [What It Does](#what-it-does)
- [How We Built It](#how-we-built-it)
- [Challenges We Faced](#challenges-we-faced)
- [How to Run](#how-to-run)
- [Tech Stack](#tech-stack)
- [Team](#-Team)

---

## 🎯 Introduction
This project focuses on Gen AI-driven risk analysis for financial transactions. It processes payment transactions, extracts entities, checks for sanctions, analyzes news and financial filings, and evaluates risk using an AI-powered approach. The goal is to enhance compliance monitoring and financial risk detection.

## 🎥 Demo
🔗 [Video Demo](https://drive.google.com/file/d/1zfLjbGGiQM5OJMs8UFQ7v0u38tvk6duo/view?usp=sharing ) (Pls check it from Google Drive since Github has a limitation for 25mb)  
🖼️ Screenshots:
UI:
![image](https://github.com/user-attachments/assets/b5f3ecdd-d65c-4e31-861b-aadb5a6d41c6)

File Parsed Successfully:
![image](https://github.com/user-attachments/assets/b4f73a2d-6f90-4966-8c37-63640582ae62)

Risk Analysis:

![image](https://github.com/user-attachments/assets/6345fc2f-47ff-49b8-a297-ba131eaa1460)


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
   ```
   https://github.com/ewfx/aidel-calculated-chaos.git
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
- **Database:** PostgreSQL (If Needed)
- **NLP Models:** BERT/BART, OpenAI API
- **Financial APIs:** SEC Edgar
- **LLM:** Llama 3 8B Model, GEMMA 3 1B, 

## 👥 Team
- **Keerthana Sureshkumar**
- **S. Rohith**
- **Vishal Ramesh K**
- **Vinay Pandey** 


## 🎯 Conclusion
This AI-powered risk analysis system enhances financial compliance by automating entity screening, risk assessment, and regulatory checks. By leveraging LLMs, NLP models, and financial data sources, it ensures accurate and transparent decision-making in financial transactions.
