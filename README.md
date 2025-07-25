# Gears Site — FastAPI + Telegram заявки

## Описание

Этот проект — сервер на FastAPI для приёма заявок с сайта и автоматической отправки их в Telegram (в определённую тему группы).

---

## Быстрый старт

1. **Клонируй репозиторий:**
   ```sh
   git clone https://github.com/v01cee/gears_site.git
   cd gears_site
   ```

2. **Создай и активируй виртуальное окружение (по желанию):**
   ```sh
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   source .venv/bin/activate  # Linux/Mac
   ```

3. **Установи зависимости:**
   ```sh
   pip install -r requirements.txt
   # или вручную:
   pip install fastapi uvicorn requests python-dotenv
   ```

4. **Создай файл `.env` в корне проекта:**
   ```env
   TELEGRAM_TOKEN=твой_токен_бота
   TELEGRAM_CHAT_ID=твой_chat_id
   TOPIC_ID=твой_topic_id
   ```

5. **Запусти сервер:**
   ```sh
   uvicorn gears.main:app --reload --port 8080
   ```

6. **Открой документацию:**
   http://localhost:8080/docs

---

## Как получить chat_id и topic_id для Telegram

1. Добавь бота в группу, сделай админом.
2. Напиши сообщение в нужную тему (топик).
3. Открой:
   ```
   https://api.telegram.org/bot<ТВОЙ_ТОКЕН>/getUpdates
   ```
4. В ответе найди:
   - `chat.id` — это chat_id
   - `message_thread_id` — это topic_id

---

## Пример запроса

```json
{
  "fio": "Иванов Иван",
  "phone": "+79991234567",
  "question": "Хочу узнать подробнее",
  "contacts": ["Телефон", "Telegram"]
}
```

---

## Лицензия

MIT 