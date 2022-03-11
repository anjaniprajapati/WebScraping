from meraki_task_1 import scrap_top_list
import json
colect_of_task_1=scrap_top_list()
def group_by_year(movies):
    years=[]
    movies_dict={}
    for i in movies:
        year=i["Year"]
        if year not in years:
            years.append(year)
    movies_dict={i:[] for i in years}
    for i in movies:
        year=i["Year"]
        for j in movies_dict:
            if str(j)==str(year):
                movies_dict[j].append(i)
    with open("meraki_task_2.json","w")as file:
        json.dump(movies_dict,file,indent=6)
    return movies_dict  
group_by_year(colect_of_task_1)