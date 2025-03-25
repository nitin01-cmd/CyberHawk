from scapy.all import sniff
import sqlite3
import logging

# Setup Logging
logging.basicConfig(filename="network_honeypot.log", level=logging.INFO)

# Database Setup
conn = sqlite3.connect("honeypot_logs.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS network_scans (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ip TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")
conn.commit()

def packet_callback(packet):
    if packet.haslayer("IP"):
        ip = packet["IP"].src
        logging.info(f"[SCAN] Unauthorized scan detected from {ip}")

        # Store in DB
        cursor.execute("INSERT INTO network_scans (ip) VALUES (?)", (ip,))
        conn.commit()

print("[+] Network Honeypot running...")
sniff(prn=packet_callback, store=0)
