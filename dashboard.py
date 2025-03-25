from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# Fetch attack data from the database
def get_attack_data():
    conn = sqlite3.connect("honeypot_logs.db")
    cursor = conn.cursor()

    # Get total attack counts
    cursor.execute("SELECT COUNT(*) FROM web_logins")
    web_count = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM ssh_attempts")
    ssh_count = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM network_scans")
    scan_count = cursor.fetchone()[0]

    # Get latest attack attempts
    cursor.execute("SELECT ip, username, password, timestamp FROM web_logins ORDER BY timestamp DESC LIMIT 5")
    web_attacks = cursor.fetchall()

    cursor.execute("SELECT ip, username, password, timestamp FROM ssh_attempts ORDER BY timestamp DESC LIMIT 5")
    ssh_attacks = cursor.fetchall()

    cursor.execute("SELECT ip, timestamp FROM network_scans ORDER BY timestamp DESC LIMIT 5")
    scan_attacks = cursor.fetchall()

    conn.close()
    
    return web_count, ssh_count, scan_count, web_attacks, ssh_attacks, scan_attacks

@app.route('/')
def dashboard():
    web_count, ssh_count, scan_count, web_attacks, ssh_attacks, scan_attacks = get_attack_data()
    return render_template("dashboard.html", web_count=web_count, ssh_count=ssh_count, scan_count=scan_count,
                           web_attacks=web_attacks, ssh_attacks=ssh_attacks, scan_attacks=scan_attacks)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
