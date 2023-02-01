import requests
from bs4 import BeautifulSoup

class TestCrawling:

    title = ''

    def test_crawling(self):
       
        url = 'https://news.daum.net/'

        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        self.title = soup.find(class_='tit_g').text