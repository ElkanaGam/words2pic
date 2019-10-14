from google_images_download import google_images_download   #importing the library


'''
    function for downloading the translated word
    return the word , and the downloaded picture location to be opened by
    the create_grid module
'''
def pic_download(word):
    response = google_images_download.googleimagesdownload()   #class instantiation

    arguments = {"keywords":word +" clipart","limit":1,"color":"red", "print_urls":False,"usage_rights":"labeled-for-reuse"}   #creating list of arguments
    
    paths = response.download(arguments)   #passing the arguments to the function

    #return (word, path)
    print(paths)   #printing absolute paths of the downloaded images
