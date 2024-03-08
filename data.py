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