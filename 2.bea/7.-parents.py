from bs4 import BeautifulSoup

def  get_context(path):
    with open(path, 'r') as file:
        return file.read()

if __name__ == '__main__':
    content = get_context('..\\requests\\econpy.html')
    bs = BeautifulSoup(content, 'html.parser')
    
    span = bs.find('span', {'class': 'item-price'})
    print(span.parent.parent.name)

    for parent in span.parents:
        print(parent.name)