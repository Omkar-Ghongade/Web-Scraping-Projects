# Flipkart I-phone 

from bs4 import BeautifulSoup
import requests

page=requests.get("https://www.flipkart.com/search?q=iphones&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")

page.content

soup=BeautifulSoup(page.content,'html.parser')

print(soup.prettify())

mobiles=soup.find_all("div",class_='_13oc-S')

print(len(mobiles))

names=[]
price=[]
ratings=[]
for mobile in mobiles:
  name=mobile.find("div",class_='_4rR01T').text
  names.append(name)

  prices=mobile.find("div",class_='_30jeq3 _1_WHN1').text
  price.append(prices)

  rate=mobile.find("div",class_='gUuXy')
  rateing=mobile.find("div",class_='_3LWZlK').text
  ratings.append(rateing)
  
import pandas as pd

dic={'Name':names,'Prices':price,"Ratings":ratings}
df=pd.DataFrame(dic)
df.to_csv('mobile_info.csv')
