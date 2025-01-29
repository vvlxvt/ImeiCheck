import asyncio
import logging
import sys
from threading import Thread

import aiohttp
from flask import Flask, request, jsonify
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from functions import IsValidUser, is_valid_imei

# TOKEN = getenv("BOT_TOKEN")
TOKEN = '8077941644:AAFQzB5cP1TVmSaQFn-elxFJlRGS0zgqT2A'
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()
app = Flask(__name__)

# Куклы для проверки IMEI
dummy_imei_db = {
    "490154203237518": {"brand": "Samsung", "model": "Galaxy S21", "status": "Clean"},
    "987654321098765": {"brand": "Apple", "model": "iPhone 13", "status": "Blacklisted"},
}


API_TOKEN = "your_api_token"

@app.route("/api/check-imei", methods=["POST"])
def check_imei_api():
    try:
        data = request.json
        if not data or not isinstance(data, dict):
            return jsonify({"status": "error", "message": "Некорректный JSON"}), 400

        imei = data.get("imei")
        token = data.get("token")

        if not imei or not token:
            return jsonify({"status": "error", "message": "IMEI и токен обязательны"}), 400

        if not isinstance(imei, str):
            return jsonify({"status": "error", "message": "IMEI должен быть строкой"}), 400

        if token != API_TOKEN:
            return jsonify({"status": "error", "message": "Неверный токен"}), 403

        if not is_valid_imei(imei):
            return jsonify({"status": "error", "message": "Неверный формат IMEI"}), 400

        imei_info = dummy_imei_db.get(imei)
        if not imei_info:
            return jsonify({"status": "error", "message": "IMEI не найден в базе"}), 404

        response = {"status": "success", "imei": imei, **imei_info}
        return jsonify(response)

    except Exception as e:
        return jsonify({"status": "error", "message": f"Внутренняя ошибка сервера: {str(e)}"}), 500


API_URL = "http://127.0.0.1:5000/api/check-imei"

WHITELIST = {541172529, 123456789, 987654321}
dp.message.middleware(IsValidUser(WHITELIST))

@dp.message(Command("start"))
async def start(message: Message):
    await message.answer("Введите IMEI для проверки:")

@dp.message()
async def check_imei_handler(message: Message):
    imei = message.text.strip()

    if not is_valid_imei(imei):
        await message.answer("❌ Неверный формат IMEI. Введите 15-значный номер.")
        return

    await message.answer(f"🔄 Проверяю IMEI: {imei}...")

    async with aiohttp.ClientSession() as session:
        async with session.post("http://127.0.0.1:5000/api/check-imei",
                                json={"imei": imei, "token": API_TOKEN}) as response:
            data = await response.json()

    if data["status"] == "error":
        await message.answer(f"❌ Ошибка: {data['message']}")
    else:
        await message.answer(f"✅ Найден: {data['brand']} {data['model']}\n📌 Статус: {data['status']}")


def run_flask():
    app.run(host="127.0.0.1", port=5000, debug=False)

async def main() -> None:

    # Запускаем Flask в отдельном потоке
    flask_thread = Thread(target=run_flask, daemon=True)
    flask_thread.start()

    # Запускаем Telegram-бота
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())