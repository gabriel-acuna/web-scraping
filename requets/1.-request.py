import requests
import re

URL = 'http://econpy.pythonanywhere.com/ex/001.html'

if __name__ == '__main__':
    response = requests.get(URL)
    if response.status_code == 200:
        content = response.text
        # with open('econpy.html', 'w+') as file:
        #     file.write(content)
        opener_tag = '<div title="buyer-name">'
        close_tag ='</div>'
        for line in content.split('\n'):
            if opener_tag in line:
                start = line.find(opener_tag) + len(opener_tag)
                end = line.find(close_tag)
                title = line[start:end]
                print(title)
            

        