from fastapi import FastAPI, Request
import uvicorn
from indmdev_telegram_bot import send_alert_to_telegram
from indmdev_db import log_alert
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

@app.post('/webhook')
async def webhook_listener(request: Request):
    data = await request.json()
    
    symbol = data.get('symbol')
    signal_type = data.get('signal_type')
    entry = data.get('entry')
    sl = data.get('stop_loss')
    tp = data.get('take_profit')
    timestamp = data.get('timestamp')
    
    alert_message = f"""
🚨 *Trading Alert* 🚨

📌 *Pair*: `{symbol}`
📈 *Signal*: `{signal_type}`

🎯 *Entry*: `{entry}`
🛑 *Stop Loss*: `{sl}`
✅ *Take Profit*: `{tp}`

🕒 *Time*: `{timestamp}`
"""

    telegram_response = send_alert_to_telegram(alert_message)
    log_alert(symbol, signal_type, entry, sl, tp, timestamp)
    
    return {
        "success": True,
        "telegram_response": telegram_response
    }

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
