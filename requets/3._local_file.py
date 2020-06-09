import re


if __name__ == '__main__':
    with open('econpy.html', 'r') as file:
        content = file.read()
        regex = '<div title="buyer-name">(.+?)</div>'
        
        for buyer in re.findall(regex, content): 
            print(buyer)
