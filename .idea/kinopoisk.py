import requests
from bs4 import BeautifulSoup

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}

URL = 'https://rezka.ag/films/fiction/'

response = requests.get(url=URL, headers=HEADERS)

soup = BeautifulSoup(response.content, 'html.parser')
arr = []

items = soup.find_all('div', class_='b-content__inline_item-link')
for item in items:
    arr.append({
        'title': item.find('a').get_text(),
        'link': item.find('a').get('href'),
        'years': item.find('div').get_text()
    })


def filter_years(arr: list, year:int):
    new_fims = []
    for i, j in enumerate(arr):
        years = int(j['years'][:4])
        if years > year:
            new_fims.append(j)
    return new_fims

films = filter_years(arr, 2014)