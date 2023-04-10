from bs4 import BeautifulSoup as bs
import requests
def telegram(username):
    base_url= f"https://telegram.dog/{username}"
    r= requests.get(base_url).text
    #print(r)
    soup = bs(r,"lxml")
    members = soup.find("div",class_="tgme_page_extra").text.split("subscribers")[0].replace(" ","")
    #print(members)
    title = soup.find("div", class_="tgme_page_title").text
    #print(title)
    data= []
    data["members"]=members
    data["title"]= title
    return data






