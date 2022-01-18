# Indian Startups Data Collection

from bs4 import BeautifulSoup
import requests

page=requests.get("https://www.failory.com/startups/india")

soup=BeautifulSoup(page.content,'html.parser')

soup.prettify()

List=soup.find_all("h3")
names_of_startups=[]
for name in List:
  s=name.text
  if s[0]>='0' and s[0]<='9':
    k=s.split(' ',1)
    names_of_startups.append(k[1])
print(names_of_startups)

Details=soup.find_all("ul",role='list')
print(Details)

city=[]
year=[]
size=[]
founders=[]
funding=[]

for i in range(0,len(names_of_startups)):
  City=Details[i].find_all("li")[0].text
  City=City.split(' ',-1)
  city.append(City[-1])

  Year=Details[i].find_all("li")[1].text
  Year=Year.split(' ',-1)
  year.append(Year[-1])

  Size=Details[i].find_all("li")[4].text
  Size=Size.split(' ',-1)
  size.append(Size[-1])

  Founders=Details[i].find_all("li")[2].text
  Founders=Founders.split(' ',1)
  founders.append(Founders[1])

  Funding=Details[i].find_all("li")[5].text
  Funding=Funding.split(' ',-1)
  funding.append(Funding[-1])
  
  import pandas as pd
  
dic={'Startup Name':names_of_startups,'Founded In':year,'Founders':founders,'City':city,'Funding':funding}
df=pd.DataFrame(dic)
df.to_csv('top_Indian_Startups_info.csv')
