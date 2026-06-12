import feedparser
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# CONFIGURATION
RSS_FEEDS = [
    "https://www.frandroid.com/feed",
    "https://feeds.feedburner.com/LMI_Actualites"
]
KEYWORDS = ["Wi-Fi 7", "802.11be", "MLO", "6GHz"]
DEST_EMAIL = "ramananarivolyana@gmail.com"

# Paramètres SMTP (Exemple pour Gmail)
SMTP_SERVER = "ramananarivolyana.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "ramananarivolyana@gmail.com"
# Note : Utilisez un 'Mot de passe d'application' Google pour plus de sécurité
SENDER_PASSWORD = "lyana"

def send_email(subject, body):
    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = DEST_EMAIL
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(msg)
        server.quit()
        print("Mail envoyé avec succès !")
    except Exception as e:
        print(f"Erreur lors de l'envoi : {e}")

def check_news():
    news_found = []
    for url in RSS_FEEDS:
        feed = feedparser.parse(url)
        for entry in feed.entries:
            if any(key.lower() in entry.title.lower() for key in KEYWORDS):
                news_found.append(f"{entry.title}\nLien : {entry.link}\n")
    
    if news_found:
        body = "Nouvelles actus Veille Wi-Fi 7 détectées :\n\n" + "\n".join(news_found)
        send_email("Alerte Veille : Wi-Fi 7", body)
    else:
        body = "Il n'y a pas de nouvel article aujourd'hui pour votre veille Wi-Fi 7."
        send_email("Veille Wi-Fi 7 : Pas d'actus aujourd'hui", body)
        print("Mail de confirmation (pas d'actus) envoyé.")

if __name__ == "__main__":
    check_news()
