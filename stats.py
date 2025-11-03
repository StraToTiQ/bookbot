def get_num_words(book_contents):
    num_words = len(book_contents.split())
    return num_words

def get_num_chars(book_contents):
    book_content = book_contents.lower()
    num_chars = {}
    for ch in book_content:
        num_chars[ch] = num_chars.get(ch, 0) + 1
    return num_chars