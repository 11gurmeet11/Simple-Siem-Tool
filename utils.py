import sqlite3
from config import DB_PATH, SENDER_EMAIL, RECEIVER_EMAIL, EMAIL_SERVER, EMAIL_PORT
import smtplib
from email.mime.text import MIMEText

def collect_logs():
    """Collect logs from the database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT log_message FROM logs")
    logs = [row[0] for row in cursor.fetchall()]
    conn.close()
    return logs

def analyze_logs(logs):
    """Return only logs that contain the word 'ERROR'."""
    return [log for log in logs if 'ERROR' in log]

def send_alert(message):
    """Send an email alert with the given message."""
    msg = MIMEText(message)
    msg['Subject'] = 'SIEM Alert - Error Detected'
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECEIVER_EMAIL

    with smtplib.SMTP(EMAIL_SERVER, EMAIL_PORT) as server:
        server.starttls()
        # server.login(SENDER_EMAIL, 'your_password')  # opzionale se server richiede login
        server.send_message(msg)