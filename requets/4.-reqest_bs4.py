from bs4 import BeautifulSoup
import requests
import re

URL = 'http://econpy.pythonanywhere.com/ex/001.html'

if __name__ == '__main__':
    response = requests.get(URL)
    if response.status_code == 200:
        content = response.text
        bs = BeautifulSoup(content, 'html.parser')
        print(bs.head)