from meraki_task_4 import scrap_movie_details
from meraki_task_12 import scrape_movie_cast
import json
def scrape_movie_one(url):
    list=[]
    task_4=scrap_movie_details(url)
    task_12=scrape_movie_cast(url)
    list.append(task_4)
    list.append({"Cast":task_12})
    with open("meraki_task_13.json","w+")as file :
        json.dump(list,file,indent=6)
scrape_movie_one("https://www.rottentomatoes.com/m/toy_story_4")