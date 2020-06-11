from bs4 import BeautifulSoup
import json
def export_to_json(data):
    with open('buyers.json', 'w+') as file:
        json.dump(data,file, indent=4)

def  get_context(path):
    with open(path, 'r') as file:
        return file.read()


if __name__ == '__main__':
    buyers = [] 
    content = get_context('..\\requests\\econpy.html')
    bs = BeautifulSoup(content, 'html.parser')
    for element in bs.findAll('div',{'title':'buyer-info'}):
        buyer = element.div.text
        item_price = element.span.text
        print(f'Buyer: {buyer}    Item Price: {item_price}')
        buyers.append({'buyer':buyer, 'item_price': item_price})
    export_to_json(buyers)
           

