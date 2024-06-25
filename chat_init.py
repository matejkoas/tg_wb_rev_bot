import asyncio
from telegram import Bot

# Ваш токен бота, замените его на правильный токен, выданный @BotFather
TELEGRAM_BOT_TOKEN = '6786698502:AAG6rzZBQHuWWvQYx6FeSc4a94HLM0Z9M4I'

async def get_chat_id():
    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    updates = await bot.get_updates()
    for update in updates:
        if update.message:
            print(f"Chat ID: {update.message.chat.id}")
            print(f"Chat Type: {update.message.chat.type}")

if __name__ == '__main__':
    asyncio.run(get_chat_id())
