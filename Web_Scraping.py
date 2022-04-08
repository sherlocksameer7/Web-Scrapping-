from bs4 import BeautifulSoup
import urllib.request
import pandas as pd

page = urllib.request.urlopen("https://www.flipkart.com/search?q=iphone+12+pro+&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY")

soup = BeautifulSoup(page, "html.parser")
Product_name = soup.find('div', class_="_4rR01T")
Price = soup.find('div', class_="_30jeq3")

print(Product_name.text)
print(Price.text)

p_name = []
p_price = []
p_name.append(Product_name.text)
p_price.append(Price.text)
data = pd.DataFrame({'Product': p_name, 'Price': p_price})

print(data.head())
data.to_csv("Result.csv")