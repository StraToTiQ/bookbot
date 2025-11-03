from stats import get_num_words
from stats import get_num_chars

def get_book_text(book_path):

    with open(book_path) as f:
        book_contents = f.read()

    return book_contents

def main():
    book_path = "books/frankenstein.txt"
    book_contents = get_book_text(book_path)
    num_words = get_num_words(book_contents)
    num_chars = get_num_chars(book_contents)
    print(f"Found {num_words} total words")
    print(num_chars)
    return

main()