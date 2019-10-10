 from googletrans import Translator
 
 
 # get list of hebrew words and return yhe english translte for each one
 def my_translate (heb_words):
  #initialize the tranlate module
  translator = Translator()
  translated = []
  for w in heb_words:
   t = translator.translate(w, dest  = 'en').text
   translated.append(t)
  
  return translated
   
