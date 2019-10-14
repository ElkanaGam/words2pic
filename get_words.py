


def get_words(file_name):
    with open (file_name, encoding = 'utf-8') as f:
        print("opened")
        return f.read().split('\n')


