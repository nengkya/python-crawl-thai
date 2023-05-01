import requests
from bs4 import BeautifulSoup

keyword = 'iphone'
r = requests.get(
    ' https://render-tron.appspot.com/render/https://www.bhinneka.com/search%3Fq%3D' +
    keyword)
soup = BeautifulSoup(r.content, 'html.parser')
print(soup.find_all('div', {'id': 'catalogueProduct'}))
