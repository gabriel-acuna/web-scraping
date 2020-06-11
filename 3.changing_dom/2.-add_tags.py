from bs4 import BeautifulSoup

def  get_context(path):
    with open(path, 'r') as file:
        return file.read()

if __name__ == '__main__':
    content = get_context('..\\requests\\econpy.html')
    bs = BeautifulSoup(content, 'html.parser')
    a = bs.new_tag('a', href='https://github.com/gabriel-acuna')
    a.string = 'Github profile'
    new_tag = bs.new_tag('div', title='site-data', id='i001', class_='info' )
    new_tag.append('\n')
    new_tag.append(a)
    new_tag.append('\n')
    # append(): add the element at parent element end
    bs.body.append(new_tag)
    #insert()
    bs.body.insert(1, new_tag)
    print(bs.body)