from bs4 import BeautifulSoup

def  get_context(path):
    with open(path, 'r') as file:
        return file.read()

if __name__ == '__main__':
    content = get_context('..\\requests\\econpy.html')
    bs = BeautifulSoup(content, 'html.parser')
    div = bs.find('div', {'title':'buyer-info' })
    div['id'] = 'I0001'
    div['title'] = 'buyer-data'
    div.div.string = 'Gabriel A'
    div.span.string = '35.89'
    print(div)