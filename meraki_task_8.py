import requests
import os
from meraki_task_1 import scrap_top_list
movie = scrap_top_list()
def get_movie_list_details(a):

    for i in a:
        print(i)
        path="/home/admin123/task8/task8"+i["Movie_Name"]+".text"
        if os.path.exists(path):
            pass
        else:
            create=open(path,"w+")
            url=requests.get(i["Url"])
            create.write(url.text)

get_movie_list_details(movie)