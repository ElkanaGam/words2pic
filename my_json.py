import json


basic_cfg = {"limit":3, "print_urls":False,"silent_mode":True, "extract_metadata": True}
meta_cfg = {"Records":[]}
words = ["apple", "banana", "greep", "gold"]
path  = "./cf.json"

class JsonHandler():
    '''
        create and update config files to being pass
        to the downloader

    '''
    def __init__(self, basic_cfg, meta_cfg, path = "./args.json"):
        self.basic_cfg = basic_cfg
        self.meta_cfg = meta_cfg
        self.path = path
        
    
    def create_json (self, words):
        '''
            for every word create json args for doawnloader 
            Through cobine keywords :word to basic_cfg
            and apppend it to the meta_cfg
        '''        
        for w in words:
            w_data = self.basic_cfg.copy()
            w_data["keywords"] = w
            self.meta_cfg["Records"].append(w_data)
        with open (self.path, 'w') as f:
            json.dump(self.meta_cfg, f)


    def update_json(self,word ,field, value, path = None):
        ''''
            update the json file in the given field with the value
            the file wil be saved in the same path as before as default
        '''
        with open(self.path, 'r') as f:
            data = json.load(f)
        for e in data["Records"]:
            if e["keywords"] == word:
                e[field] = value
        if not path:
            path = self.path
        with open (path, 'w') as f:
            json.dump(data, f)



