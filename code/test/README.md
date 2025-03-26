# Transaction Screening Test Cases

## Overview
This document provides an overview of the test cases used to validate the transaction screening process. The system evaluates financial transactions against global sanctions lists, news sources, and regulatory filings to assess potential risks. Each transaction undergoes a series of checks, including:

1. **OFAC US and UN Sanctions Screening** - Verifying if entities involved in the transaction appear on the sanctions lists.
2. **News API Risk Assessment** - Analyzing news data for any negative associations with the transaction participants.
3. **SEC EDGAR Filings Review** - Checking for financial irregularities in company filings.
4. **LLM-Based Risk Scoring** - Assigning a final risk score based on extracted data and contextual risk factors.

---

## Test Cases

### **Transaction 1: OFAC US & UN Sanctions Flagged**

**Transaction ID:** TXN-2023-5AB1  
**Entities Involved:**
- **Sender:** Horizons Consulting LLC (Switzerland)
- **Receiver:** Bosco Gilan (Cayman Islands)

**Reason for Flagging:**
- The receiver entity, Bosco Gilan, appears in both the **OFAC US and UN sanctions lists**.
- Additional transaction details indicate involvement with "MUNITIONS INDUSTRY DEPARTMENT," a potential high-risk entity.
- The transaction was processed via intermediary institutions like **Quantum Holding Ltd.** and **Global FinTech Corp.**, with Switzerland as the exit node.

### **Transaction 2: OFAC UN Sanctions Flagged**

**Transaction ID:** TXN-2025-1831  
**Entities Involved:**
- **Sender:** Abdul Kabir Mohammad (Switzerland)
- **Receiver:** Bright Future Nonprofit Inc (Cayman Islands)

**Reason for Flagging:**
- The sender, Abdul Kabir Mohammad, is identified in the **OFAC UN sanctions list**.
- The transaction was routed through **Apex Capital Partners**, with an exit node in the **British Virgin Islands**, a known offshore financial jurisdiction.
- The transaction was marked as an "Urgent transaction" and was **authorized by a compliance officer, Mr. Ahmed Al-Farsi**, requiring further scrutiny.

### **Transaction 3: No Sanctions Match – Proceed to News & SEC Checks**

**Transaction ID:** TXN-2021-7653  
**Entities Involved:**
- **Sender:** Walmart
- **Receiver:** Wells Fargo

**Outcome:**
- No matches found in **OFAC US or UN sanctions lists**.
- The system proceeds with **News API analysis** to verify any negative media coverage related to Walmart and Wells Fargo.
- If no significant risk indicators are found, the **SEC EDGAR database is queried** for financial irregularities in Walmart's and Wells Fargo's filings.
- After completing these checks, the **LLM risk scoring model** assigns a final risk rating to the transaction.

