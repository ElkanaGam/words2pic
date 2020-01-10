from googletrans import Translator
import get_words 
 
 # get list of hebrew words and return yhe english translte for each one
def my_translate (heb_words):
  #initialize the tranlate module
  print("tranlation starting")
  translator = Translator()
  translated = []
  for w in heb_words:
    
    try:
        t = translator.translate(w, dest  = 'en').text
        translated.append(t)
    except:
        print(w," translation failed")
  
  print("translation ending")
  return translated



