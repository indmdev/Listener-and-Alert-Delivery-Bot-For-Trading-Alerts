import requests
import os
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

def send_alert_to_telegram(message):
    api_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown",
        "reply_markup": {
            "inline_keyboard": [
                [
                    {"text": "✅ Confirm", "callback_data": "confirm_trade"},
                    {"text": "❌ Ignore", "callback_data": "ignore_trade"}
                ]
            ]
        }
    }
    response = requests.post(api_url, json=payload)
    return response.json()
