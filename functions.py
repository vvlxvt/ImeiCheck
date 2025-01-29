import re
from aiogram.dispatcher.middlewares.base import BaseMiddleware
from aiogram.types import Message


class IsValidUser(BaseMiddleware):
    def __init__(self, whitelist: set):
        self.whitelist = whitelist
        super().__init__()

    async def __call__(self, handler, event: Message, data):
        if event.from_user.id not in self.whitelist:
            await event.answer("⛔ У вас нет доступа к боту.")
            return
        return await handler(event, data)

def is_valid_imei(imei):
    """Проверяем IMEI по алгоритму Луна"""
    if not isinstance(imei, str) or not re.fullmatch(r"\d{15}", imei):
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