import json

import requests

from bs4 import BeautifulSoup


class Scraper(object):
    def __init__(self):
        self.url = 'https://www.nation.co.ke'
    
    def scrape_site(self):
        res = requests.get(self.url)
        file = BeautifulSoup(res.content, 'html.parser')

        for teaser in file.find_all('div', class_='story-teaser medium-teaser'):
            title = teaser.div.p.text
            print(title)
            print()


scrape = Scraper()
print(scrape.scrape_site())