import json
with open("meraki_task_5.json","r")as file:
    movies_data=json.load(file)
def analyse_movies_directors ():
    directors_dict={}
    for i in movies_data:
        if 'Director' in i:
            directer=i['Director']
            for j in directer:
                if j in directors_dict:
                    directors_dict[j]+=1
                else:
                    directors_dict[j]=1
    with open("meraki_task_7.json","w+")as file:
        json.dump(directors_dict,file,indent=6)
            
analyse_movies_directors ()