### Please find demo at : https://drive.google.com/file/d/1zfLjbGGiQM5OJMs8UFQ7v0u38tvk6duo/view?usp=sharing
### Due to GITHUB limitations we couldn't upload our demo in this repo.

UI:
1. File upload UI with progress and status of steps. Also it contains features provided by our app.
![image](https://github.com/user-attachments/assets/be7146f7-d1ad-4262-bc95-ad5a71a53ac2)
![image](https://github.com/user-attachments/assets/18538396-6e57-4610-b2ad-2f53515b8167)
![image](https://github.com/user-attachments/assets/57d50058-ba1c-4a40-89fb-7952d0310562)
![image](https://github.com/user-attachments/assets/2ada3b30-5528-4310-ba13-d9ea3a3ff949)




Input Request: 

Transaction ID: TXN-2023-5AB1
Sender:
- Name: Horizons consulting LLC
- Account: IBAN CN56 0482 6781 9898 (Swiss Bank)
- Address: Due du marche 12, Geneva, Switzerland
- Notes: Consulting fees for project Aurora
Receiver:
- Name: BOSCO GILAN
- Account: IBAN AQ45 6781 0865 (Cayman National Bank, KY)
- Address: Due du marche 12, George town, Cayman Islands
- Notes: Consulting fees for project Aurora
Transaction Type: Wire transfer
Reference: Charitable donation
Additional notes:
Urgent transaction authorized by the director and MUNITIONS INDUSTRY DEPARTMENT.
Funds were transferred via Quantum Holding Ltd. and Global FinTech Corp. Exit node was Switzerland.
Approved by CEO Richard Branson at Amazon Inc.

---

Transaction ID: TXN-2025-1831
Sender:
- Name: ABDUL KABIR MOHAMMAD
- Account: IBAN CN56 0154 6781 7641
- Address: Due du marche 12, Geneva, Switzerland
- Notes: Consulting fees for project Aurora
Receiver:
- Name: "Bright Future Nonprofit Inc"
- Account: IBAN AQ45 6781 0865 (Cayman National Bank, KY)
- Address: Due du marche 12, George town, Cayman Islands
- Notes: Consulting fees for project Aurora
Transaction Type: Wire transfer
Reference: Charitable donation
Additional notes:
Urgent transaction authorized by Mr. Ahmed Al-Farsi (Chief Compliance Officer).
Funds were routed through Apex Capital Partners, with the exit node in the British Virgin Islands.

---

Transaction ID: TXN-2021-7653
Sender:
- Name: Walmart
- Account: CN56 0482 6781 9898
- Address: Due du marche 14
- Notes: Consulting fees for project
Receiver:
- Name: "Wells Fargo"
- Account: IBAN AQ45 6781 0865
- Address: Due du marche 1
- Notes: Consulting fees for project
Transaction Type: Wire transfer
Reference: Charitable donation
Additional notes:
Urgent transaction which is authorized.txt…]()

Output Response:
```
{
  "Risk_Assessment_Results": [
    {
      "Transaction_ID": "TXN-2023-5AB1S",
      "Extracted_Entities": [
        "Horizons consulting LLC",
        "Swiss Bank",
        "BOSCO GILAN",
        "Cayman National Bank",
        "MUNITIONS INDUSTRY DEPARTMENT",
        "Quantum Holding Ltd",
        "Global FinTech Corp",
        "Richard Branson",
        "Amazon Inc"
      ],
      "Entity_Type": [
        "Corporation",
        "Corporation",
        "Corporation",
        "Corporation",
        "Corporation",
        "Corporation",
        "Corporation",
        "Individual",
        "Corporation"
      ],
      "Risk_Score": 0.9153,
      "Supporting_Evidence": ["OFAC US Sanctions"],
      "Confidence_Score": 0.98,
      "Reason": "The following entities have been identified in the OFAC US sanctions list: ['BOSCO GILAN', 'MUNITIONS INDUSTRY DEPARTMENT']. Engaging with sanctioned entities poses regulatory, financial, and reputational risks."
    },
    {
      "Transaction_ID": "TXN-2025-1831S",
      "Extracted_Entities": [
        "ABDUL KABIR MOHAMMAD",
        "Bright Future Nonprofit Inc",
        "Cayman National Bank",
        "Ahmed Al",
        "Farsi",
        "Apex Capital Partners"
      ],
      "Entity_Type": [
        "Individual",
        "Corporation",
        "Corporation",
        "Individual",
        "Individual",
        "Corporation"
      ],
      "Risk_Score": 0.8,
      "Supporting_Evidence": ["OFAC UN Sanctions"],
      "Confidence_Score": 0.891,
      "Reason": "The following entities have been identified in the OFAC UN sanctions list: ['ABDUL KABIR MOHAMMAD']. Engaging with sanctioned entities poses regulatory, financial, and reputational risks."
    },
    {
      "Transaction_ID": "TXN-2021-7653",
      "Extracted_Entities": ["Walmart", "Wells Fargo"],
      "Entity_Type": ["Corporation", "Corporation"],
      "Risk_Score": 0.4628,
      "Confidence_Score": 0.8,
      "Supporting_Evidence": [
        "Google news",
        "Edgar",
        "LLM Knowledge"
      ],
      "Reason": {
        "Walmart": "Walmart filed 4 on Unknown Date: Discloses insider trading, which could indicate undisclosed risks or potential misconduct. Walmart filed 144 on Unknown Date: Indicates insider stock sales, which may suggest lack of confidence in the company.",
        "Wells Fargo": "Wells Fargo: corruption (0.36) - Potential risk based on negative news coverage."
      }
    }
  ]
}
```

