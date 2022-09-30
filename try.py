def count_words(filename):
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass
    else:
        print(contents.lower().count('the'))

file_name = 'file/book.txt'
count_words(file_name)