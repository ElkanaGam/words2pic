import get_words
import translator
import downloader
def main ():
    lst = translator.my_translate(get_words.get_words("my_file.txt"))
    print("translation ending")
    for w in lst:
        downloader.pic_download(w)

main()
    