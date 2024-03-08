import pandas as pd
import datetime

def addData(productName, url, price):
    """Save data into data.csv file if data was not saved today
    Args :
        productName (str) : the name of the product to save
        url (str) : product's url
        price (int) : product price
    Returns :
        bool : True if data was saved, False else"""
    data = pd.read_csv("data.csv", sep=";")
    today = datetime.date.today()
    if len(data) > 0:
        if len(data[(data["date"] == str(today)) & (data["productUrl"] == url)]) <= 0:
            newFrame = pd.DataFrame(data={"date":[today], "productName":[productName], "productUrl":[url], "price":[price]})
            data = data.append(newFrame)
            data.to_csv("data.csv", index=False, sep=";")
            return True
        else:
            return False
    else:
        newFrame = pd.DataFrame(data={"date": [today], "productName": [productName], "productUrl": [url], "price": [price]})
        data = data.append(newFrame)
        data.to_csv("data.csv", index=False, sep=";")
        return True

def getLastData(csvFile):
    """Get last product's datas from specified CSV file and returns it.
    Args :
        csvFile (str) : the date, product name, product url and product price containing CSV file's address
    Returns :
        list : contains 3 list : first contains list of products'url (str), second contains product's name (str), third contains product's price (int)"""
    data = pd.read_csv(csvFile, sep=";")
    data = data.sort_values(by=["date"], ascending=False) ##sorting data by dates, from older to latest

    productsUrl = []
    productsName = []
    productsPrice = []
    for index in range(len(data)):
        url = data["productUrl"].iloc[index]
        if url not in productsUrl: ##checking if this product was already traited
            productsUrl.append(url)
            productsName.append(data["productName"].iloc[index])
            productsPrice.append(data["price"].iloc[index])

    return [productsUrl, productsName, productsPrice]

