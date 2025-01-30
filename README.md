# Flask Web Application
Простое веб-приложение на Flask для обработки пользовательских форм с использованием TinyDB для хранения данных. 

## Требования

- Python 3.12
- Flask 3.x
- TinyDB 4.x
- pytest (для тестов)

## Структура проекта

```plaintext
ProjectWebApp/
├── checkapp/
│   ├── __init__.py       # Инициализация приложения Flask, регистрация маршрутов и Blueprints
│   ├── db.py             # Создание экземпляра базы данных (TinyDB)
│   ├── routes.py         # Определение маршрутов и обработчиков запросов
│   ├── models.py         # Добавление данных в БД
│   ├── utils.py          # Вспомогательные функции (валидация данных)
│   └── send_post.py      # Пример отправки POST-запроса в приложение через Python
├── tests/
│   ├── test_validate_field.py  # Тесты для функции валидации данных
├── db.json              # Локальный файл базы данных для хранения информации
├── app.py               # Точка входа в приложение, запуск сервера Flask
└── requirements.txt     # Файл зависимостей для установки библиотек
```
## Установка

1. Клонируйте репозиторий:
    ```bash
    git clone https://github.com/vvlxvt/WebApp
    ```

2. Установите зависимости:
    ```bash
    pip install flask tinydb pytest
    ```

## Запуск

Запустите приложение с помощью команды:
   ```bash
   python app/app.py
   ```
## Конфигурация

```markdown
- Настройки базы данных можно изменить в файле `db.py`.
- Для добавления новых шаблонов форм, измените файл `app/models.py`.
```
## Примеры использования

**Тестирование**

Запустите тесты с помощью pytest:

```bash
.venv\Scripts\activate
set PYTHONPATH=.
pytest -v tests\test_validate_field.py

```
### Отправка формы через CURL
Отправьте POST-запрос на `/get_form`:
```bash
curl -X POST -d "email=user@example.com&phone=+75556661122" http://127.0.0.1:5000/get_form
```

### Замечание
В curl '+' может интерпретироваться как пробел.
Замените '+' на '%2B' в curl:
```bash
curl -X POST -d "email=user@example.com&phone=%2B75556661122" http://127.0.0.1:5000/get_form
```


## Контакты

Если у вас есть вопросы, пишите на [vvlxvt@gmail.com](vvlxvt@gmail.com).