from telegram import Bot
from telegram.error import InvalidToken

# Замените 'YOUR_TELEGRAM_BOT_TOKEN' на ваш токен
TELEGRAM_BOT_TOKEN = '6786698502:AAG6rzZBQHuWWvQYx6FeSc4a94HLM0Z9M4I'

try:
    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    print("Токен действителен!")
except InvalidToken:
    print("Неверный токен. Проверьте правильность токена.")
