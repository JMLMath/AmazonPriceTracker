import bs4
import requests

def getPrice(url, priceCSSSelector, position=1):
    """Arguments :
        url (str) : The website url
        priceCSSSelector (str) : The CSS selector of the html element what contains price
        position (int) : Position of the element of all elements of this class (1 by default)
    Returns :
        float : the price"""
    request = requests.get(url)
    soup = bs4.BeautifulSoup(request.text, "html.parser")
    priceElem = soup.select(priceCSSSelector)[position] ##price take the position element of the list of all priceCSSSelector element
    price = priceElem.text[1:] ##for removing the '$' caracter at the begining
    return float(price)

def getName(url, nameCSSSelector, position=0):
    """Arguments :
        url (str) : The website url
        nameCSSSelector (str) : the CSS selector of the html elemnt what contains product name
        position (int) : Position of the element of all elements of this CSS class (1 by default)
    Returns :
        str : the product name"""
    request = requests.get(url)
    soup = bs4.BeautifulSoup(request.text, "html.parser")
    nameElem = soup.select(nameCSSSelector)[position]
    name = nameElem.text
    return name

