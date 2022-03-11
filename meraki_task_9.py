import os
import json
import random
import time
with open("meraki_task_5.json","r+")as file:
    movie_details=json.load(file)
def movies_file():
    random_no=random.randint(1,3)
    for i in movie_details:
        path="/home/admin123/task9/task9"+i["name"]+".json"
        if os.path.exists(path):
            pass
        else:
            with open(path,"w+")as f:
                json.dump(i,f,indent=6)
        
        time.sleep(random_no)


movies_file()