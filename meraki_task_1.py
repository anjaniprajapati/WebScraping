import requests
from bs4 import BeautifulSoup
import json
url=requests.get("https://www.rottentomatoes.com/top/bestofrt/top_100_animation_movies/")
soup=BeautifulSoup(url.text,"html.parser")
def scrap_top_list():
    
    main_div=soup.find("div",class_="panel-body content_body allow-overflow")
    table=main_div.find("table",class_="table")
    tes=table.find_all("tr")
    list=[]
    for i in tes:
        
        td=i.find_all("td")
        dict={}
        for j in td:
            
            rank=i.find("td","bold").get_text()[:-1]
            dict["Movie_Rank"]=int(rank)
            
            rating=i.find("span",class_="tMeterScore").get_text()[1:3]
            dict["Movie_Rating"]=float(rating)
            
            name=i.find("a","unstyled articleLink")["href"][3:]
            dict["Movie_Name"]=name

            reviews=i.find("td",class_="right hidden-xs").get_text()
            dict["Movie_Reviews"]=int(reviews)

            year=i.find("a","unstyled articleLink").get_text()[-5:-1]
            dict["Year"]=int(year)

            link=i.find("a","unstyled articleLink")["href"]
            url="https://www.rottentomatoes.com"+link
            dict["Url"]=url
    
        list.append(dict)
    if {} in list:
        list.remove({})
    with open("meraki_task_1.json","w")as file:
        json.dump(list,file,indent=6)
    
    return list
scrap_top_list()