from bs4 import BeautifulSoup
import urllib.request
import pandas as pd

page = urllib.request.urlopen("https://www.flipkart.com/search?q=iphone+12+pro+&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY")

soup = BeautifulSoup(page, "html.parser")

# Product_name = soup.find('div', class_="_4rR01T")
# Price = soup.find('div', class_="_30jeq3")

# print(Product_name.text)
# print(Price.text)

p_name = []
p_price = []

for i in soup.findAll("div", class_="_3pLy-c row"):
    get_Product = i.find("div", attrs={"class": "_4rR01T"})
    get_Price = i.find("div", attrs={"class": "_30jeq3 _1_WHN1"})
    # get_Star_Rating = i.find("div", attrs={"class": "_3LWZlK"})
    # get_Features = i.find("div", attrs={"class": "rgWa7D"})

    p_name.append(get_Product.text)
    p_price.append(get_Price.text)


# p_name.append(Product_name.text)
# p_price.append(Price.text)

data = pd.DataFrame({'Product': p_name, 'Price': p_price})

print(data.head())
data.to_csv("Result.csv")