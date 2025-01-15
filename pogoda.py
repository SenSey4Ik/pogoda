import requests
from bs4 import BeautifulSoup
import lxml

#Ссылка на сайт
url='https://yandex.ru/pogoda/biysk?lat=52.54181&lon=85.220652'

#Данные, чтобы сайт понимал, что зашел человек, а не бот
headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}

#Отправляем запрос на сайт с командой получить
response = requests.get(url, headers=headers)

# просим у сайта вернуть красиво отформатированный текст
soup = BeautifulSoup(response.text, 'lxml')

#Парсим класс в котором хранится погода
data = soup.find('div', class_= "temp fact__temp fact__temp_size_s")

#Из данного кода вытягиваем только градусы
temp = data.text

def sinh_pog():
    """100 раз выводим погоду в Бийске"""
    for i in range(100):
        print(f'В Бийске сейчас:{temp} градусов')

sinh_pog()