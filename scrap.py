from bs4 import BeautifulSoup
import requests
from openpyxl import Workbook
workbook = Workbook()
sheet = workbook.active
article_title=[]
article_author=[]


page = requests.get("https://sadaf.mrsservers.com:8443/smb/log-file/browser/id/769")

soup = BeautifulSoup(page.content, 'html.parser')

s_id2= soup.findAll('div',attrs={'class':'brand-collapsed'})
s_id1= soup.findAll('tbody.tr.td',attrs={'class':'number state-default'})
s_id= soup.findAll('td',attrs={'class':'number'})

s_t = soup.findAll('td',attrs={'class':"number state-default"})

for i in range(0,len(soup1)):
         article_title.append(s_id2[i].text)
         article_author.append(s_id[i].text)
print("page{} : ".format(j),article_title)
print(s_id)
print(s_t)

cnt=0
for i in range(0,len(article_author)):
    for j in range(0,len(article_author[i])):
        cnt+=1
        sheet["A{}".format(cnt)] = article_title[i][j]
        sheet["B{}".format(cnt)] = article_author[i][j]
workbook.save(filename="hello_world.xlsx")