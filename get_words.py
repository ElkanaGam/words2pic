


def get_words(file_name):
  with open (file_name, encoding = 'utf-16') as f:
    return f.read().split('\n')
