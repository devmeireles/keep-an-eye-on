import urllib
import requests
import re
from bs4 import BeautifulSoup as bs
from helpers.treat_data import TreatData


class Crawler():

    @staticmethod
    def get_data():
        query = "Electrolux"
        query = query.replace(' ', '+')
        URL = f"https://google.com/search?hl=en&q={query}"

        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}

        resp = requests.get(URL, headers=headers)

        data = []

        if resp.status_code == 200:
            soup = bs(resp.content, "html.parser")

            content = soup.select(
                ".kp-wholepage.kp-wholepage-osrp > .osrp-blk > .Kot7x > #kp-wp-tab-cont-overview > #kp-wp-tab-overview > .cLjAic.LMRCfc > div > div > div")

            if content:

                for item in content:
                    for i in range(len(item.select('div'))):
                        arr = TreatData.handle_keys(item.select('div')[i].text)

                        data.append(arr)

            data = TreatData.avoid_keys(data)

        return data
