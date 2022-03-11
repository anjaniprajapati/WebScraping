from bs4 import BeautifulSoup
import requests
import json
from meraki_task_1 import scrap_top_list

def scrap_movie_details(movie_url):
    page=requests.get(movie_url)
    soup=BeautifulSoup(page.text,'html.parser')
    # print(soup)
    li=soup.find_all("li",class_="meta-row clearfix")
    name=soup.find("h1",class_="scoreboard__title").get_text()
    dict={}
    movie=scrap_top_list()
    for i in li:
        k=i.text
        n=k.split()
        # print(n)
        for j in n:
            if 'Rating'in  j:
                dict["name"]=name
                dict["Rating"]=n[1]

            if 'Genre' in j:
                a=n[1:]
                n=""
                for i in a:
                    n+=i
                n=n.split(",")
                dict["Genre"]=n

            if 'Original' in j:
                dict["Language"]=n[2]

            if 'Director' in j:
                a=n[1:]
                s=""
                for i in a:
                    s+=i
                s=s.split(",")
                dict["Director"]=s
            
            if "Writer" in j:
                a=n[1:]
                x=""
                for i in a:
                    x+=i
                x=x.split(",")
                dict["Writer"]=x

            if "Producer" in j:
                a=n[1:]
                h=""
                for i in a:
                    h+=i
                h=h.split(",")
                dict["Producer"]=h
            
            if "Release" in j:
                dict["Release"]=n[3:6]
            if "Runtime" in j:
                time=n[1:]
                
                i=0
                while i<len(time):
                    hour=time[0][0]
                    mint=time[1]
                    min=mint[:-1]
                    i=i+1
                Rom=int(hour)*60+int(min)
                dict["Runtime"]=Rom
    with open("meraki_task_4.json","w+")as file:
        json.dump(dict,file,indent=6)
        return dict

scrap_movie_details("https://www.rottentomatoes.com/m/toy_story_4")