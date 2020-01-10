import json


basic_cfg = {"limit":3, "print_urls":False,"silent_mode":True, "extract_metadata": True}
meta_cfg = {"Records":[]}
words = ["apple", "banana", "greep", "gold"]
path  = "./cf.json"
def update_json(path,word ,field, value):

    with open(path, 'r') as f:
        data = json.load(f)
    for e in data["Records"]:
        if e["keywords"] == word:
            e[field] = value
    with open (path, 'w') as f:
        json.dump(data, f)

def create_json (path, words):        
    for w in words:
        w_data = basic_cfg.copy()
        w_data["keywords"] = w
        meta_cfg["Records"].append(w_data)
    with open (path, 'w') as f:
        json.dump(meta_cfg, f)


#create_json(words)

#update_json(path, "apple", "limit", 2)