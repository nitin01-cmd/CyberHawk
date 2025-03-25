import paramiko
import socket
import threading
import sqlite3
import logging

# Setup Logging
logging.basicConfig(filename="ssh_honeypot.log", level=logging.INFO)

# Database Setup
conn = sqlite3.connect("honeypot_logs.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS ssh_attempts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ip TEXT,
    username TEXT,
    password TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")
conn.commit()

# Fake SSH Server Config
host_key = paramiko.RSAKey.generate(2048)

class SSHServer(paramiko.ServerInterface):
    def check_auth_password(self, username, password):
        ip = client.getpeername()[0]
        logging.info(f"[SSH] Intruder Detected! IP: {ip}, Username: {username}, Password: {password}")

        # Store in DB
        cursor.execute("INSERT INTO ssh_attempts (ip, username, password) VALUES (?, ?, ?)", (ip, username, password))
        conn.commit()

        return paramiko.AUTH_FAILED

# Start the SSH Honeypot
def start_ssh_honeypot():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 2222))
    server.listen(5)
    print("[+] SSH Honeypot running on port 2222...")

    while True:
        global client
        client, addr = server.accept()
        transport = paramiko.Transport(client)
        transport.add_server_key(host_key)
        ssh_server = SSHServer()
        transport.start_server(server=ssh_server)

ssh_thread = threading.Thread(target=start_ssh_honeypot)
ssh_thread.start()
