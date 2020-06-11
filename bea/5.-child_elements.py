from bs4 import BeautifulSoup

def  get_context(path):
    with open(path, 'r') as file:
        return file.read()

if __name__ == '__main__':
    content = get_context('..\\requests\\econpy.html')
    bs = BeautifulSoup(content, 'html.parser')
    div = bs.find('div', {'title': 'buyer-info'})
    buyer = div.contents[1].text
    price = div.contents[3].text
    print(buyer, price)

    for child in div.children:
        print(child)