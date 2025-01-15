import requests
from bs4 import BeautifulSoup
import lxml

def sinh_pog():
    """Синхронно вызываем get запрос 100 раз"""

    #Ссылка на сайт
    url='https://yandex.ru/pogoda/biysk?lat=52.54181&lon=85.220652'

    for i in range(100):
        #Отправляем запрос на сайт с командой получить
        response = requests.get(url)

        # просим у сайта вернуть красиво отформатированный текст
        soup = BeautifulSoup(response.text, 'lxml')

        #Парсим класс в котором хранится погода
        data = soup.find('div', class_= "temp fact__temp fact__temp_size_s")

        #Вытягиваем температуру
        temp = data.text

        print(f'В Бийске сейчас: {temp} градусов')

sinh_pog()