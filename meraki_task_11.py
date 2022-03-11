import json
with open("meraki_task_5.json","r+")as file:
    movie_list=json.load(file)
# print(movie_list)
def analyse_movies_genre():
    gener_dict={}
    for i in movie_list:
        if "Genre" in i:
            gener=i["Genre"]
            for j in gener:
                if j in gener_dict:
                    gener_dict[j]+=1
                else:
                    gener_dict[j]=1
    with open("meraki_task_11.json","w+")as file:
        json.dump(gener_dict,file,indent=6)           

analyse_movies_genre()