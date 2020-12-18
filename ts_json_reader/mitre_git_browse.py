# from github import Github
# ACCESS_TOKEN = '9064021cc01dc7694818577cb473d9bff1141278'
#g = Github(ACCESS_TOKEN)
#print(g.get_user().get_repos())

import json
import os 
path = "C:\\Users\\jorge\\Documents\\python_projects\\trustar_screener\\ts_json_reader\\mitre_json"

def get_mitre_json():
    f = open(os.path.join(path,"attack-pattern--0042a9f5-f053-4769-b3ef-9ad018dfa298.json"), "r")     
    x_json = json.loads(f.read())     
    return (x_json)    