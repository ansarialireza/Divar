import re
import requests
from bs4 import BeautifulSoup

url='https://divar.ir/s/tehran'
response=requests.get(url)
soup=BeautifulSoup(response.text,'html.parser')
result_1=soup.find_all('div',attrs={'class':'kt-post-card__body'})

name_list=[]
for item in result_1:
    name_list.append(item.text.strip())
new_list=[]
for i in name_list:
    
    new_list.append(i)

for i in new_list:
    print(i,'\n')

