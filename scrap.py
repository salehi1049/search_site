from msilib.schema import tables
from bs4 import BeautifulSoup
import requests
import pandas as pd
from openpyxl import Workbook

workbook = Workbook()
sheet = workbook.active
article_title=[]
article_author=[]

# tables=pd.read_html("https://sadaf.mrsservers.com:8443/smb/log-file/browser/id/769")
# df1=tables[0]
# temp=df1.head()
page1 = requests.get("https://virgool.io/python-community/%D8%A7%D8%B3%D8%AA%D8%AE%D8%B1%D8%A7%D8%AC-%D8%A7%D8%B7%D9%84%D8%A7%D8%B9%D8%A7%D8%AA-%D8%A7%D8%B2-%D8%B5%D9%81%D8%AD%D8%A7%D8%AA-%D9%88%D8%A8-%D8%A8%D8%A7-python-oztzkyxir0az")
soup = BeautifulSoup(page1.text, "html.parser")

page = requests.get("https://sadaf.mrsservers.com:8443/smb/log-file/browser/id/769")
soup = BeautifulSoup(page.text, "html.parser")

# soup_e= soup.find("tr",attrs={"class":"even"})
# soup_o= soup.find("tr",attrs={"class":"odd"})

s_id1= soup.find_all("td",attrs={"class":"number state-default"})
s_id = soup.find_all('td',attrs={'class':'number'})

s_t = soup.find_all('td',attrs={'class':"number state-default"})

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