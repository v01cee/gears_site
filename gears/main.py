from fastapi import FastAPI
from .models import RequestForm
from .tg import send_to_telegram

app = FastAPI()

@app.post("/api/request")
async def submit_request(form: RequestForm):
    send_to_telegram(form)
    return {"status": "ok", "message": "Заявка отправлена!"} 