from flask import Flask, request, jsonify
import re

app = Flask(__name__)

# Тестовые данные для проверки IMEI
dummy_imei_db = {"123456789012345": {"brand": "Samsung", "model": "Galaxy S21", "status": "Clean"},
    "987654321098765": {"brand": "Apple", "model": "iPhone 13", "status": "Blacklisted"}}

# Тестовый токен API
API_TOKEN = "your_api_token"


def is_valid_imei(imei):
    """Проверяет IMEI по алгоритму Луна"""
    if not re.fullmatch(r"\d{15}", imei):
        return False
    total = 0
    for i, digit in enumerate(reversed(imei)):
        n = int(digit)
        if i % 2 == 1:
            n *= 2
            if n > 9:
                n -= 9
        total += n
    return total % 10 == 0


@app.route("/api/check-imei", methods=["POST"])
def check_imei():
    data = request.json
    imei = data.get("imei")
    token = data.get("token")

    if not imei or not token:
        return jsonify({"status": "error", "message": "IMEI и токен обязательны"}), 400

    if token != API_TOKEN:
        return jsonify({"status": "error", "message": "Неверный токен"}), 403

    if not is_valid_imei(imei):
        return jsonify({"status": "error", "message": "Неверный формат IMEI"}), 400

    imei_info = dummy_imei_db.get(imei)
    if not imei_info:
        return jsonify({"status": "error", "message": "IMEI не найден в базе"}), 404
    lk
    response = {"status": "success", "imei": imei, **imei_info}
    return jsonify(response)
    для


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)


