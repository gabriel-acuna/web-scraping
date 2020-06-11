from bs4 import BeautifulSoup

def  get_context(path):
    with open(path, 'r') as file:
        return file.read()

if __name__ == '__main__':
    content = get_context('..\\requests\\econpy.html')
    bs = BeautifulSoup(content, 'html.parser')
    #1
    div1 = bs.find('div', {'title': 'buyer-name'})
    #2 
    div2 = bs.find('div', string='Carson Busses')

    print(div1, div2)
    ''' 
     Access to nodes
        next_sibling
        previous_sibling
    '''
    print(div2.next_sibling.next_sibling)

    for element in div1.next_siblings:
        print(element)

    