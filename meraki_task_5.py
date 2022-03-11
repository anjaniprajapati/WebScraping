import json
from meraki_task_1 import scrap_top_list
from meraki_task_4 import scrap_movie_details
movies_data=scrap_top_list()
def get_movie_list_details():
    list=[]
    for i in movies_data:
        k=i["Url"]
        # print(k)
        a=scrap_movie_details(k)
        list.append(a)
        # print(list)
    with open("meraki_task_5.json","w+")as file1:
        json.dump(list,file1,indent=4)
        return list
get_movie_list_details()