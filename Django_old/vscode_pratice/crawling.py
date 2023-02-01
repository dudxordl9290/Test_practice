import requests
from bs4 import BeautifulSoup

url = 'https://news.daum.net/'

response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
title = soup.find(class_='tit_g').text
print(title)
