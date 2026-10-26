from fastapi import FastAPI, Request
import uuid

app = FastAPI()

# Это наш "рюкзак" для заявок (пока сервер работает, заявки хранятся тут)
leads_db = []

# 1. Сюда будет стучаться ВАШ САЙТ, когда клиент заполнит форму
@app.post("/api/webhook")
async def receive_lead(request: Request):
    data = await request.json()
    # Добавляем уникальный номер заявке
    data["id"] = str(uuid.uuid4()) 
    leads_db.append(data)
    return {"status": "ok"}

# 2. Сюда будет стучаться ВАШЕ ПРИЛОЖЕНИЕ на iPhone, чтобы забрать заявки
@app.get("/api/leads")
async def get_leads():
    return leads_db