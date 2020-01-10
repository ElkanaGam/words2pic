from google_images_download import google_images_download   #importing the library
import my_json
import json


'''
    function for downloading the translated word
    return the word , and the downloaded picture location to be opened by
    the create_grid module
'''


class Downloader ():

    def __init__(self, img_type, cfg_use = False):
        
        self.img_dwnldr  = google_images_download.googleimagesdownload() 
        self.img_type = " "+img_type
        self.basic_cfg = {"keywords":"","socket_timeout":1,"limit":3, "print_urls":False,"silent_mode":False, "extract_metadata": True}
        self.meta_cfg = {"Records":[]}
        self.cfg_use = cfg_use
    
    def pic_download(self, words):
        words =  [(word+ self.img_type) for word in words]
        handler = my_json.JsonHandler(self.basic_cfg, self.meta_cfg)
        handler.create_json(words)
        if self.cfg_use:
            #download multyple words if cfguse = True using the cfg_file
            self.img_dwnldr.download({"config_file": handler.path})
        else:
            #download only one word
            self.basic_cfg["keywords"] = words[0]
            self.img_dwnldr.download(self.basic_cfg)

    def second_try(self,word,  field, value, clipart = True):
        self.basic_cfg["keywords"] = word+self.img_type
        self.basic_cfg[field] = value
        self.img_dwnldr.download(self.basic_cfg)

