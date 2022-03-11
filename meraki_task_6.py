import json 
with open("meraki_task_5.json","r")as file:
    movies_data=json.load(file)
    # print(movies_data)
def analyse_movie_language():
    langua_dict={}
    for i in movies_data:
        # print(i)
        if "Language" in i:
            l=[i["Language"]]
            for j in l:
                # print(j)
                if j not in langua_dict:
                    langua_dict[j]=1
                    # print(langua_dict)
                else:
                    langua_dict[j]+=1
    with open("meraki_task_6.json","w+")as file_1:
        json.dump(langua_dict,file_1,indent=6)


analyse_movie_language()