import json
with open("meraki_task_5.json","r+")as file:
    movies_details=json.load(file)
def analyse_language_and_directors():
    dic={}
    list=[]
    for i in movies_details:
        for j in i["Director"]:
            if j not in list:
                list.append(j)
    for i in list:
        dic1={}
        for j in movies_details:
            if i in j["Director"]:
                if "Language" in j:
                    language=j["Language"]
                    if language  in  dic1:
                        dic1[language]+=1
                    if language not in dic1:
                       dic1[language]=1
                dic[i]=dic1
    with open("meraki_task_10.json","w+") as file:
        json.dump(dic,file,indent=4)

analyse_language_and_directors()