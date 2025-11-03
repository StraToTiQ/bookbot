def get_num_words(book_contents):
    num_words = len(book_contents.split())
    return num_words

def get_num_chars(book_contents):
    book_content = book_contents.lower()
    num_chars = {}
    for ch in book_content:
        num_chars[ch] = num_chars.get(ch, 0) + 1
    return num_chars

def sort_on(items):
    return items["num"]

def get_sorted_list_num_chars (num_chars):
    list_chars = []
    for key in num_chars:
        list_chars.append({"char": key, "num": num_chars[key]})
    list_chars.sort(reverse=True, key=sort_on)
    return list_chars