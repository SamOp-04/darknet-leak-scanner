# core/alert.py (updated)
import smtplib
from email.message import EmailMessage
import sqlite3

def check_alert_terms(alert_terms):
    conn = sqlite3.connect('data/leaks.db')
    cursor = conn.cursor()
    alerts_found = []
    
    for term in alert_terms:
        cursor.execute("SELECT * FROM leaks WHERE email LIKE ?", ('%' + term + '%',))
        if matches := cursor.fetchall():
            alerts_found.extend(matches)
            print(f"\n[!] ALERT: Found '{term}' in {len(matches)} records!")
            for row in matches:
                print(f"  - {row[1]} @ {row[2]} ({row[3]})")
    
    if alerts_found:
        send_email_alert(alerts_found, alert_terms)

def send_email_alert(alerts, terms):
    msg = EmailMessage()
    msg.set_content(f"Darknet Alert!\n\nFound {len(alerts)} matches for {terms}:\n\n" +
                    "\n".join(f"{row[1]} @ {row[2]} ({row[3]})" for row in alerts))
    
    msg['Subject'] = f"DARKNET ALERT: {len(alerts)} matches found!"
    msg['From'] = "alert@yourdomain.com"
    msg['To'] = "admin@yourdomain.com"
    
    try:
        with smtplib.SMTP('smtp.server.com', 587) as server:
            server.starttls()
            server.login("user", "pass")
            server.send_message(msg)
        print("Alert email sent!")
    except Exception as e:
        print(f"Email failed: {e}")