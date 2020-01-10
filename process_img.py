from __future__ import print_function

from PIL import Image
import os, sys
import json


#root dir
#need to open every dir separatly
#convert all types to jpg
#resize
#save in outer dir

    

class Process_IMG ():

    #args are the search parameteres: name clipart , reuse, color 
    def __init__(self, *args):
        self.c_dir = os.getcwd()    #currrent dir of the running program, it is the "root" +/downloads?
        self.files = os.listdir(self.c_dir)
        self.pic_name = args[0] # word
        self.pic_type = args[1] #  type(clipatr, black  and white etc)
        self.suffix = self.pic_name+self.pic_type
    
    def __repr__(self):
        return self.c_dir

    def contain_img(self):
        path = self.c_dir+"/downloads/" + self.suffix
        return os.listdir(path) != []

    def is_suitable_img (self, img_name):
        suffix = self.suffix+".json"
        path = self.c_dir+"/logs/"+ suffix
        with open(path , 'r') as file:
            data = json.load(file)
        is_suitable = False
        for img in data:
            if img_name in (img["image_description"]):
                is_suitable = True
    
        return is_suitable

    #unnecceary due to docx sizing configuration
    # #def resize(self, w):
    #     for item in self.files:
    #         if os.path.isfile(self.c_dir+item):
    #             #path  = 
    #             im = Image.open(self.c_dir+item)
    #             #print(im.format, im.size, im.mode)
    #             f, e = os.path.splitext(self.c_dir+item)
    #             print(f)
    #             imResize = im.resize((200,200), Image.ANTIALIAS)
    #             #save all the resized img in one directory
    #             imResize.save(f + ' resized.jpg', 'JPEG', quality=90)
                

    # #resize()




