import requests
import re
from bs4 import BeautifulSoup as bs


def get_data(pages):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}

    url = 'https://publicacoes.estadao.com.br/empresasmais2018/ranking-1500/'

    html = requests.get(url, headers=headers)
    soup = bs(html.content, features="lxml")

    tbody = soup.select_one('.ranking-table__tbody')
    rows = tbody.find_all('div', {'class': 'ranking-table__tr'})

    items = []

    for row in rows:
        data = row.select('.ranking-table__td > span')
        name = data[1].text
        city = data[2].text
        industry = data[3].text
        revenue = data[4].text

        item = {
            'name': name,
            'city': city,
            'industry': industry,
            'revenue': revenue
        }

        items.append(item)

    return items


temp = get_data(0)

print(temp)

# print(temp)
