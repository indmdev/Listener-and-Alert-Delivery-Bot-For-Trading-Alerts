from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()
@app.post('/webhook')

async def webhook_listener(request: Request):
    data = await request.json()
    symbol = data['symbol']
    signal_type = data['signal_type']  # "LONG" or "SHORT"
    entry = data['entry']
    sl = data['stop_loss']
    tp = data['take_profit']
    timestamp = data['timestamp']
        process_alert(symbol, signal_type, entry, sl, tp, timestamp)
    return {"success": True, "message": "Alert received"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
