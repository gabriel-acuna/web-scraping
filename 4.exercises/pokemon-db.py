from bs4 import BeautifulSoup
import requests
import threading
from concurrent.futures import ThreadPoolExecutor
import time
DATA = []
def get_context(host='https://pokemondb.net',url='/pokedex/all'):
    response = requests.get(f'{host}{url}')
    if response.status_code == 200:
        context = response.text
        return BeautifulSoup(context, 'html.parser')

def get_pokemons_info():

    bs = get_context()
    table = bs.find('table', {'id': 'pokedex'})
    with  ThreadPoolExecutor(max_workers=20) as executor:
        for row in table.tbody.findAll('tr',):
            executor.submit(get_pokemon_info, row)


def get_pokemon_info(row):
    global DATA
    columns = row.findAll('td')
    id = columns[0].span.next_sibling.text
    name = columns[1].a.text
    image, species = get_spacies(url=columns[1].a.get('href'))
    type = [a.text for a in columns[2].findAll('a')]

    DATA.append({
        'id': id,
        'name': name,
        'image': image,
        'spcecies':species,
        'type': type})



def get_spacies(url):
    bs = get_context(url=url)
    grid_row = bs.find('div', {'class':['tab-panelactive','active']}).div
    table = bs.find('table', class_='vitals-table')
    image = grid_row.div.p.a.get('href')
    species = table.tbody.findAll('tr')[2].td.text
    return image, species


if __name__ == '__main__':
  
    t1= threading.Thread(target=get_pokemons_info)
    t1.start()
    t1.join()
    print(f'{time.perf_counter()} seconds process time')

    print(DATA)
   
          
