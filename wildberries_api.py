import requests
import time


def get_reviews(token):


    # Параметры запроса
    params = {
        'isAnswered': 'false',  # true для обработанных отзывов, false для необработанных
        'take': 10,  # Количество отзывов для получения
        'skip': 0,  # Количество отзывов для пропуска
        'dateFrom': int(time.time()) - 3600 * 24 * 7,  # Пример: отзывы за последние 7 дней
        'dateTo': int(time.time())  # Текущая дата в формате Unix timestamp
    }

    # URL API (замените на реальный URL)
    api_url = 'https://feedbacks-api.wildberries.ru/api/v1/feedbacks'  # Замените на фактический URL API

    # Заголовки запроса
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }

    # Выполнение запроса
    response = requests.get(api_url, headers=headers, params=params)

    # Проверка успешности запроса
    if response.status_code == 200:
        data = response.json()
        #print(data)
    else:
        print(f"Ошибка: {response.status_code}")
        #print(response.text)

    return data
