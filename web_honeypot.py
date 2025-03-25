from flask import Flask, request
import sqlite3
import logging

app = Flask(__name__)

# Setup Logging
logging.basicConfig(filename="web_honeypot.log", level=logging.INFO)

# Database Setup
conn = sqlite3.connect("honeypot_logs.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS web_logins (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ip TEXT,
    username TEXT,
    password TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")
conn.commit()

@app.route('/admin', methods=['GET', 'POST'])
def fake_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        ip = request.remote_addr

        # Log intrusion attempt
        logging.info(f"[WEB] Intruder Detected! IP: {ip}, Username: {username}, Password: {password}")
        cursor.execute("INSERT INTO web_logins (ip, username, password) VALUES (?, ?, ?)", (ip, username, password))
        conn.commit()

        return "Access Denied", 403
    
    return '''
        <h2>Admin Login</h2>
        <form method="post">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Login">
        </form>
    '''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
