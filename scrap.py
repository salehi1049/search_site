from bs4 import BeautifulSoup
import requests

page = requests.get("https://sadaf.mrsservers.com:8443/login_up.php?success_redirect_url=%2Fsmb%2Flog-file%2Fbrowser%2Fid%2F769")

soup = BeautifulSoup(page.content, 'html.parser')

s_id = soup.find_all(class_ ="number")

s_t = soup.find_all(class_="number state-default")

tonight = forecast_items[0]
print(tonight.prettify())
###############
period = tonight.find(class_ = "period-name").get_text()
short_Desc = tonight.find(class_ = "short-desc").get_text()
temp = tonight.find(class_ = "temp temp-high").get_text()

print(period)
print(short_Desc)
print(temp)
