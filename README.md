# **CyberHawk - AI-Powered Honeypot for Cyber Threat Intelligence**  

[![GitHub Repo](https://img.shields.io/badge/GitHub-CyberHawk-blue?style=flat&logo=github)](https://github.com/nitin01-cmd/CyberHawk)

## **🔒 Overview**  
CyberHawk is an advanced **AI-powered honeypot system** designed to **detect, log, and analyze cyber attacks** in real time. It simulates vulnerable systems to attract attackers, logs their activities, and helps security professionals monitor potential threats.

## **🚀 Features**  
### **✅ Completed (Phase 1 & Phase 2)**
- **Web Honeypot** → Fake admin login panel that logs unauthorized login attempts.
- **SSH Honeypot** → Simulated SSH server that captures brute-force attacks.
- **Network Scan Detection** → Monitors and logs unauthorized port scanning.
- **Centralized Logging** → Stores all attack data in a structured database.
- **Real-Time Monitoring** → Captures attacker IPs, login attempts, and timestamps.
- **Basic Dashboard (In Progress)** → Web-based dashboard to visualize attack trends.

### **🔮 Future Developments**
- **AI-powered Threat Detection** → Machine learning to identify advanced attack patterns.
- **Automated IP Blocking** → Use `iptables` & `fail2ban` for real-time threat mitigation.
- **Live Attack Alerts** → Integration with Telegram & Email notifications.
- **Cloud Deployment** → Deploying on AWS/DigitalOcean for real-world testing.

## **🛠 Tech Stack & Libraries**  
- **Programming Language:** Python 🐍  
- **Framework:** Flask (for Web & API)  
- **Database:** SQLite (for attack logs)  
- **Networking:** Paramiko (SSH), Scapy (Port Scanning Detection)  
- **Visualization:** Chart.js (for data visualization in the dashboard)  

## **📥 Installation & Setup**  
### **1️⃣ Clone the Repository**  
```bash
 git clone https://github.com/nitin01-cmd/CyberHawk.git 
 cd CyberHawk
```

### **2️⃣ Install Dependencies**  
```bash
pip install flask paramiko scapy flask-sqlalchemy
```

### **3️⃣ Run the Web Honeypot**  
```bash
python web_honeypot.py
```
Visit **http://localhost:5000/admin** and test by entering random credentials.

### **4️⃣ Run the SSH Honeypot**  
```bash
python ssh_honeypot.py
```
Try connecting using:  
```bash
ssh fakeuser@localhost -p 2222
```

### **5️⃣ Run the Network Scanner Detection**  
```bash
python network_honeypot.py
```
Run an Nmap scan to test:  
```bash
nmap -p 22,80,5000,2222 localhost
```

### **6️⃣ Run the Dashboard (In Progress)**  
```bash
python dashboard.py
```
Visit **http://localhost:8080/** to view attack stats.

## **📌 Contribution**  
Want to improve CyberHawk? Contributions are welcome! Fork the repo and submit a PR. 🚀

## **📄 License**  
This project is licensed under the **MIT License**.

---
### **🌟 Follow the Project on GitHub:** [CyberHawk](https://github.com/nitin01-cmd/CyberHawk)
