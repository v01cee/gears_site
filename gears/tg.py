import os
import requests
from dotenv import load_dotenv
from .models import RequestForm

# Явно указываем путь к .env
load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))

# Отладочные print'ы
print("PWD:", os.getcwd())
print("TOKEN:", os.getenv("TELEGRAM_TOKEN"))
print("CHAT_ID:", os.getenv("TELEGRAM_CHAT_ID"))
print("TOPIC_ID:", os.getenv("TOPIC_ID"))

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = int(os.getenv("TELEGRAM_CHAT_ID"))
TOPIC_ID = int(os.getenv("TOPIC_ID"))

def send_to_telegram(form: RequestForm):
    text = (
        f"Новая заявка!\n"
        f"ФИО: {form.fio}\n"
        f"Телефон: {form.phone}\n"
        f"Вопрос: {form.question or '-'}\n"
        f"Связаться через: {', '.join(form.contacts) if form.contacts else '-'}"
    )
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": text,
        "message_thread_id": TOPIC_ID
    }
    requests.post(url, data=payload) 