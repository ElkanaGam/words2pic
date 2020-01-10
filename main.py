import get_words
import translator
import downloader
import os
import json
import process_img
import my_json 
import time
import threading
class Timer():
    
    def __enter__(self):
        self.start = time.time()

    def __exit__(self, err,e, t ):
        print(time.time()-self.start)


    
def main ():
    with Timer ():
        src_words = get_words.get_words("my_file.txt")
        trans_words = translator.my_translate(src_words)
        words = dict(zip(src_words, trans_words))
        #downloading images for every word in lst
        threads = []
        d = downloader.Downloader("clipart", cfg_use=False)
        for w in trans_words:
            thread = threading.Thread(target=d.pic_download, args = ([w],))
            threads.append(thread)
        for t in threads:
            t.start()
        for t in threads:
            t.join()        
        
        # #check if the folder contains images for the word
        for w in trans_words:
            process_tool = process_img.Process_IMG(w, " clipart")
            limit = 10
            while not process_tool.contain_img():
                #to be completed bt second_try function 
                print (w + " not found ")
                d.second_try(w, "limit", limit)
                limit += 5
            
            while (limit < 20 )and (not process_tool.is_suitable_img(w)):
                #to be completed bt second_try function 
                print (w + " is not fitting ")
                d.second_try(w, "limit", limit)
                limit += 5
                
            
        #     process_tool.resize(w)


    # #validate_img(lst[0])

main()
    