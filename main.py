from wildberries_api import get_reviews
import asyncio
from telegram import Bot, Update
from telegram.ext import Application, CommandHandler, ContextTypes



TELEGRAM_BOT_TOKEN = '6786698502:AAG6rzZBQHuWWvQYx6FeSc4a94HLM0Z9M4I'
CHAT_ID = '246095137'  # ID чата, куда будут отправляться уведомления

# Инициализация бота
bot = Bot(token=TELEGRAM_BOT_TOKEN)

# Инициализация Updater с использованием объекта Bot и update_queue
updater = Updater(bot=bot, update_queue=None)
dispatcher = updater.dispatcher

token_wb1 = 'eyJhbGciOiJFUzI1NiIsImtpZCI6IjIwMjQwMjI2djEiLCJ0eXAiOiJKV1QifQ.eyJlbnQiOjEsImV4cCI6MTcyNjc5NDg1MywiaWQiOiJjYzEwNDI2ZS05YWEwLTRmZmQtODgwYy01MDI3ZDQzOWRkNmQiLCJpaWQiOjM2MDgyNTM3LCJvaWQiOjc0NTA3LCJzIjoxMDczNzQyMzM0LCJzaWQiOiJlYWU5Y2I4Yy1lMGFlLTU1ODMtOGViOC04ZTBlYWRkOTc0ZTYiLCJ0IjpmYWxzZSwidWlkIjozNjA4MjUzN30.gwcvDQhh-tb0ZZHJfgzBbLxCKJtplSnek3RzriOxgabWGuhmcJBQuyyd5G2X8_NvJWmnzYHPTW0fX5gXiWg8ow'
token_wb2 = 'eyJhbGciOiJFUzI1NiIsImtpZCI6IjIwMjQwMjI2djEiLCJ0eXAiOiJKV1QifQ.eyJlbnQiOjEsImV4cCI6MTcyNjc5NDk0NSwiaWQiOiI2NmI1ODk5NC0xOGU4LTRmMWQtOGVmYi0xNTQzMTEzMWI2YTUiLCJpaWQiOjIzMDY4NjAxLCJvaWQiOjQxMjIyOCwicyI6MTA3Mzc0MjMzNCwic2lkIjoiNGY3NmVhYzAtNzA1Ni00Mzg5LWJhMDktYTc3ZWVlYzMzMWZjIiwidCI6ZmFsc2UsInVpZCI6MjMwNjg2MDF9.nuhLfy8emftFkBW43Vdcrva3Ih6X02cwZ6dubLzTvwPBB0HiYPsJVbczMh1u_Wf_R1O6o0mxhV3-Y9vbsy8RPw'

# Функция для отправки сообщений о негативных отзывах
async def send_negative_reviews(token):
    reviews_data = get_reviews(token)

    if 'data' in reviews_data and 'feedbacks' in reviews_data['data']:
        feedbacks = reviews_data['data']['feedbacks']

        for review in feedbacks:
            product_valuation = review.get('productValuation', 0)
            if isinstance(product_valuation, int) and product_valuation < 3:
                text = review.get('text', 'Отсутствует текст отзыва')
                createdDate = review.get('createdDate')
                productValuation = review.get('productValuation')
                product_details = review.get('productDetails', {})
                article = product_details.get('nmId')
                productName = product_details.get('productName')


                await bot.send_message(chat_id=CHAT_ID, text=(
                    f"Негативный отзыв: \n"
                    f"Дата и время: {createdDate}\n"
                    f"SKU: {article}\n"
                    f"Название: {productName}\n"
                    f"Оценка: {productValuation}\n"
                    f"Текст: {text}\n"

                ))

# Запуск функции проверки отзывов при запуске скрипта
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(send_negative_reviews(token_wb1))
    loop.run_until_complete(send_negative_reviews(token_wb2))

# Имя базы данных amatejkoru_tgbot
# Пароль к базе данных: 64GZwSDRSJPE!KHQ
