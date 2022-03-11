import json
from meraki_task_2 import  scrap_top_list
collect_detailse=scrap_top_list()
# print(collect_detailse)
def group_by_decade(movies):
    
    print(collect_detailse)
    movies_dict={}
    movies_list=[]
    uni_list=[]
    for i in movies:
        for j in i:
            if j=="Year":
                if i[j] not in uni_list:
                    uni_list.append(i[j])
    uni_list.sort()
    for i in uni_list:
        moduls=i%10
        mod_s=i-moduls
        if mod_s not in movies_list:
            movies_list.append(mod_s)
    for x in movies_list:
        movies_dict[x]=[]
    for x in movies_dict:
        mod_ad=x+9
        for i in movies:
            for j in i:
                if j=="Year":
                    if i[j]<=mod_ad and i[j]>=x:
                        movies_dict[x].append(i)
    print(collect_detailse)

    with open("meraki_task_3.json","w+")as file:
        json.dump(movies_dict,file,indent=6)

group_by_decade(collect_detailse)