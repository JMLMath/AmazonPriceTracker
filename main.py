from webRequest import *
from data import *


VERSION = [0,1]

def main():
    print(f"Amazon price tracker v.{VERSION[0]}.{VERSION[1]}")
    print("Opening productList.txt...")
    with open("productList.txt","r") as productList:
        print("Reading file...")
        for url in productList.readlines():
            if url[-1] == '\n':
                url = url[:-1]
            print(f"Getting informations about {url}")
            price = getPrice(url, ".a-offscreen")
            name = getName(url, "#productTitle")
            dataAdded = addData(name, url, price)
            if dataAdded:
                print(f'Informations about "{name[:30]}" saved succesfully !')
            else:
                print(f'Informations about "{name[:30]}" was already saved today.')

if __name__ == "__main__":
    main()