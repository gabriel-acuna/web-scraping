from bs4 import BeautifulSoup

def  get_context(path):
    with open(path, 'r') as file:
        return file.read()

if __name__ == '__main__':
    content = get_context('..\\requests\\econpy.html')
    bs = BeautifulSoup(content, 'html.parser')
    div = bs.find('div', {'title':'buyer-info'})
    #1
    div.span.contents = []
    #2
    div.span.string = ''
    # remove tag
    div.span.extract()
    print(div)
