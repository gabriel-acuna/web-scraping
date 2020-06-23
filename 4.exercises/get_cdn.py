import re
import requests
import urllib.request
import time
from bs4 import BeautifulSoup

import sys, getopt

def make_request(url):
    response = requests.get(url)
    if response.status_code == 200:
        return BeautifulSoup(response.text, 'html.parser')

def get_react_cdn():
    url = 'https://es.reactjs.org/docs/add-react-to-a-website.html'
    bs = make_request(url)
    targets = bs.findAll('span', class_ = 'token attr-value')
    links = []
    print('\n --------- React ----------\n')
    for t in targets:
        if t.find(string=re.compile('^https')):
            links.append(t.contents[2])
    print(f'''
-------- Development --------
        "{links[0]}"
        "{links[1]}"

-------- Production --------
        "{links[2]}"
        "{links[3]}"

-------- Babel --------
        "{links[4]}"
        
    ''')

def get_vue_cdn():
    url = 'https://vuejs.org/v2/guide/'
    bs = make_request(url)
    targets = bs.select('.hljs-string',limit=2)
    print('\n --------- Vue ----------\n')
    print(f'''
-------- Development --------
    {targets[0].string}
    

-------- Production --------
    {targets[1].string}
    
''')

def get_bulma_cdn():
    url = 'https://data.jsdelivr.com/v1/package/npm/bulma'
    last_version = requests.get(url).json().get('tags').get('latest')
    bulma = f'"https://cdn.jsdelivr.net/npm/bulma@{last_version}/css/bulma.css"'
    bulma_min = f'"https://cdn.jsdelivr.net/npm/bulma@{last_version}/css/bulma.min.css"'
    print('\n --------- Bulma ----------\n')
    print(bulma, '\n', bulma_min)

def get_bootstrap_cdn():
    url = 'https://getbootstrap.com/'
    bs = make_request(url)
    a = bs.find('a', class_='btn btn-lg btn-bd-primary mb-3 mr-md-3')
    last_version =a['href']
    bs =  make_request(f'{url}{last_version[1:]}')
    links = bs.findAll('code',{'class':'language-html', 'data-lang':'html'})
    link_css, js = '', ''
    for text in links[0]:
        link_css += f'{text.string} '
    for text in links[1]:
        if text.string == '&gt;&lt;/script&gt;': js += '\n\n'
        js += text.string
    print('\n --------- Bootstrap ----------\n', '\n******** css *********\n', link_css, '\n******** js *********\n', js )

def show_options():
    print('''
        This script let you get cdn for React, Vue o Bulma
        **** Options ****
            -h / --help: Show you how to use this script
            -v: Get Vue cdn
            -r: Get React cdn
            --bulma: Get Bulma cdn
            --bootstrap: Get Bootstrap cdn
    ''')

def options_handler(argv):
    try:
        if len(argv) == 0: print('-h / --help: Show you how to use this script')
        options = getopt.getopt(argv,'hvr',['bulma', 'bootstrap','help'])
        
    except getopt.GetoptError:
        print('get_cdn.py -h  for help')
        sys.exit(2)
    
    for o in options[0]:
        if o in ('-h', '--help'):
            show_options()
        elif o[0] =='-v':
            get_vue_cdn()
        elif o[0] == '-r':
            get_react_cdn()
        elif o[0] == '--bulma':
            get_bulma_cdn()
        elif o[0] == '--bootstrap':
            get_bootstrap_cdn()
            
   


if __name__ == "__main__":
    options_handler(sys.argv[1:])
   