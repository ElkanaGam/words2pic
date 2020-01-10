


def get_words(file_name):
    print("opening "+ file_name)
    with open (file_name, encoding = 'utf-8') as f:
        print("file was opend")
        return f.read().split('\n')


