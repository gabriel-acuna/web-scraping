import requests
from bs4 import BeautifulSoup
import datetime
HOST = 'https://news.google.com'
def get_contex(url='/topics/CAAqLQgKIidDQkFTRndvSkwyMHZNR1ptZHpWbUVnWmxjeTAwTVRrYUFsVlRLQUFQAQ?hl=es-419&gl=US&ceid=US%3Aes-419'):
    response = requests.get(f'{HOST}{url}')
    if response.status_code == 200:
        return BeautifulSoup(response.text, 'html.parser')

if __name__ == '__main__':
    bs = get_contex()
    with open(f"news/news_{datetime.datetime.now().strftime('%d-%m-%Y')}.txt", 'w+') as file:

        file.write(f'\nDate: {datetime.datetime.now()} \n\n')
        file.write(f'\n\n -------- NEWS ---------\n\n')
        for h3 in  bs.find_all('h3', class_='ipQwMb ekueJc gEATFF RD0gLb'):
            title = h3.a.text
            url = f"{HOST}{h3.a['href']}"
            file.write(f'title: {title} \n url: {url}\n\n')
