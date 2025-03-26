[sample_input.txt](https://github.com/user-attachments/files/19470007/sample_input.txt)Please find demo at : https://drive.google.com/file/d/1zfLjbGGiQM5OJMs8UFQ7v0u38tvk6duo/view?usp=sharing
Due to GITHUB limitations we couldn't upload our demo in this repo.

UI:
1. File upload UI with progress and status of steps. Also it contains features provided by our app.
![image](https://github.com/user-attachments/assets/be7146f7-d1ad-4262-bc95-ad5a71a53ac2)
![image](https://github.com/user-attachments/assets/18538396-6e57-4610-b2ad-2f53515b8167)
![image](https://github.com/user-attachments/assets/57d50058-ba1c-4a40-89fb-7952d0310562)



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


🛡️ Risk Assessment Results
🔹 Transaction 1
{
"Transaction ID":"TXN-2023-5AB1S"
"Extracted Entity":[
0:"Horizons consulting LLC"
1:"Swiss Bank"
2:"BOSCO GILAN"
3:"Cayman National Bank"
4:"MUNITIONS INDUSTRY DEPARTMENT"
5:"Quantum Holding Ltd"
6:"Global FinTech Corp"
7:"Richard Branson"
8:"Amazon Inc"
]
"Entity Type":[
0:"Corporation"
1:"Corporation"
2:"Corporation"
3:"Corporation"
4:"Corporation"
5:"Corporation"
6:"Corporation"
7:"Individual"
8:"Corporation"
]
"Risk Score":0.9153
"Supporting Evidence":[
0:"OFAC US Sanctions"
]
"Confidence Score":0.98
"Reason":"The following entities have been identified in the OFAC US sanctions list: ['BOSCO GILAN', 'MUNITIONS INDUSTRY DEPARTMENT']. Engaging with sanctioned entities poses regulatory, financial, and reputational risks."
}
🔹 Transaction 2
{
"Transaction ID":"TXN-2025-1831S"
"Extracted Entity":[
0:"ABDUL KABIR MOHAMMAD"
1:"Bright Future Nonprofit Inc"
2:"Cayman National Bank"
3:"Ahmed Al"
4:"Farsi"
5:"Apex Capital Partners"
]
"Entity Type":[
0:"Individual"
1:"Corporation"
2:"Corporation"
3:"Individual"
4:"Individual"
5:"Corporation"
]
"Risk Score":0.8
"Supporting Evidence":[
0:"OFAC UN Sanctions"
]
"Confidence Score":0.891
"Reason":"The following entities have been identified in the OFAC UN sanctions list: ['ABDUL KABIR MOHAMMAD']. Engaging with sanctioned entities poses regulatory, financial, and reputational risks."
}
🔹 Transaction 3
{
"Transaction ID":"TXN-2021-7653"
"Extracted Entity":[
0:"Walmart"
1:"Wells Fargo"
]
"Entity Type":[
0:"Corporation"
1:"Corporation"
]
"Risk Score":0.4628
"Confidence Score":0.8
"Supporting Evidence":[
0:"Google news"
1:"Edgar"
2:"LLM Knowledge"
]
"Reason":{
"Walmart":"Walmart filed 4 on Unknown Date: Discloses insider trading, which could indicate undisclosed risks or potential misconduct. | Walmart filed 4 on Unknown Date: Discloses insider trading, which could indicate undisclosed risks or potential misconduct. | Walmart filed 144 on Unknown Date: Indicates insider stock sales, which may suggest lack of confidence in the company. | Walmart filed 4 on Unknown Date: Discloses insider trading, which could indicate undisclosed risks or potential misconduct. | Walmart filed 4 on Unknown Date: Discloses insider trading, which could indicate undisclosed risks or potential misconduct. - https://news.google.com/rss/articles/CBMigwFBVV95cUxNQnAtVkVOQmRUVDF5eDZHQjhZd1oxRkxMQWxCNUFESzROV3NOYVphS0JVcFpfcXdueVVxZGVUdlRub1EyZ3ZNUlRlVlh6OUZsc05UTTJNd1hOODRlT0pYVkM1Y3c2blZSbm5WVk9ZNkFnLTJ5RktOUXVVWXNCNlVPR3JVVdIBiAFBVV95cUxOOTctbndjR1N4blNLeHMxb05qX3RFN2FfOFV3bU9RNklPNWFsQVo2T2VYQllDOUJBVjRZbE53RzIzNXlxbWluRHJVTEJPRWhDX1ZNV01BSVduQ1NQYUM1eVpTUmgtWm9hOC1OcmtOYjFQNU1UNE1jZkpwR1ZGc3VFemkzVTMtMGlj?oc=5"
"Wells Fargo":"Wells Fargo: corruption (0.36) - https://news.google.com/rss/articles/CBMigwFBVV95cUxNQnAtVkVOQmRUVDF5eDZHQjhZd1oxRkxMQWxCNUFESzROV3NOYVphS0JVcFpfcXdueVVxZGVUdlRub1EyZ3ZNUlRlVlh6OUZsc05UTTJNd1hOODRlT0pYVkM1Y3c2blZSbm5WVk9ZNkFnLTJ5RktOUXVVWXNCNlVPR3JVVdIBiAFBVV95cUxOOTctbndjR1N4blNLeHMxb05qX3RFN2FfOFV3bU9RNklPNWFsQVo2T2VYQllDOUJBVjRZbE53RzIzNXlxbWluRHJVTEJPRWhDX1ZNV01BSVduQ1NQYUM1eVpTUmgtWm9hOC1OcmtOYjFQNU1UNE1jZkpwR1ZGc3VFemkzVTMtMGlj?oc=5"
}
}

