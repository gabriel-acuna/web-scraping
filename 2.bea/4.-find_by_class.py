from bs4 import BeautifulSoup

def  get_context(path):
    with open(path, 'r') as file:
        return file.read()

if __name__ == '__main__':
    buyers = [] 
    content = get_context('..\\requests\\econpy.html')
    bs = BeautifulSoup(content, 'html.parser')
    #1
    print('\n-------- using tag param --------\n')
    for item_price in bs.findAll('span', {'class':'item-price'}):
        print(item_price.get_text())
    #2 
    print('\n-------- using attrs param --------\n')
    for item_price in bs.findAll(attrs={'class':'item-price'}):
        print(item_price.get_text())
    #3
    print('\n-------- using class_ param --------\n')
    for item_price in bs.findAll(class_='item-price'):
        print(item_price.get_text())
