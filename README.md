# Телеграм бот IMEI
Бэкенд-система для проверки IMEI устройств, которая интегрирована с Telegram-ботом и предоставляет API для внешних запросов

## Требования

- Python 3.12
- Flask 3.x
- aiogram==3.x
- pytest==8.x
- requests 2.x

## Структура проекта

```plaintext
ImeiCheck/
├── tests/
│   ├── fake_request.py  # Тесты для функции валидации данных
│   └── test_valid_imei.py  # Тесты для функции валидации IMEI
├── app.py               # Точка входа в приложение, запуск сервера Flask
├── utils.py          # Вспомогательные функции (валидация данных)
└── requirements.txt     # Файл зависимостей для установки библиотек
```
## Установка

1. Клонируйте репозиторий:
    ```bash
    git clone https://github.com/vvlxvt/ImeiCheck
    ```

2. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```

## Запуск

Запустите приложение из root с помощью команды:
   ```bash
   python app.py
   ```
## Конфигурация

```markdown
- Для добавления telegram ID измените в файле `app.py` WHITELIST.
- Для изменения адреса и порта приложения Flask измените параметры app.run() в файле `app.py`.
```
## Примеры использования

**Тестирование функции валидности IMEI**

Запустите тесты с помощью pytest:

```bash
.venv\Scripts\activate
set PYTHONPATH=.
pytest -v tests\test_validate_imei.py
```
**Тестирование запроса через API c помощью requests**

Запустите fake_request.py


**Тестирование работы API через curl командной строки**

```bash
curl -X POST http://127.0.0.1:5000/api/check-imei -H "Content-Type: application/json" -d "{\"imei\": \"490154203237518\", \"token\": \"your_secret_api_token\"}"
```


## Контакты

Если у вас есть вопросы, пишите на [vvlxvt@gmail.com](vvlxvt@gmail.com).