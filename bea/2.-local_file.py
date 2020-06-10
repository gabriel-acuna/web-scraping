from bs4 import BeautifulSoup

if __name__ == '__main__':
    with open('..\\requests\\econpy.html', 'r') as file:
        context = file.read()
        bs = BeautifulSoup(context, 'html.parser')
        title = bs.find('title')
        print(title)
        print(title.text)