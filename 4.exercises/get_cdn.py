import re
import requests
import urllib.request
import time
from bs4 import BeautifulSoup

import sys, getopt


def get_react_cdn():
    url = 'https://es.reactjs.org/docs/add-react-to-a-website.html'
    response = requests.get(url)

    print(response)

    soup = BeautifulSoup(response.text, 'html.parser')
    targets = soup.findAll('span', class_ = 'token attr-value')
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
    response = requests.get(url)
    print(response)
    soup = BeautifulSoup(response.text, 'html.parser')
    targets = soup.select('.hljs-string',limit=2)
    print('\n --------- Vue ----------\n')
    print(f'''
-------- Development --------
    {targets[0].string}
    

-------- Production --------
    {targets[1].string}
    
''')

def show_options():
    print('''
        This script let you get cdn for React or Vue
        **** Options ****
            -h: Show you how to use this script
            -v: Get Vue cdn
            -r: Get React cdn
    ''')

def options_handler(argv):
    try:
        options = getopt.getopt(argv,'hvr')
        
    except getopt.GetoptError:
        print('get_cdn.py -h  for help')
        sys.exit(2)
    
    for o in options[0]:
       
        if o[0] =='-h':
            show_options()
        elif o[0] =='-v':
            get_vue_cdn()
        elif o[0] == '-r':
            get_react_cdn()
        else:
            show_options()
   


if __name__ == "__main__":
    options_handler(sys.argv[1:])
   