def get_book_text(book_path):

    with open(book_path) as f:
        book_contents = f.read()

    return book_contents

def count_words(book_contents):
    num_words = len(book_contents.split())
    return num_words

def main():
    book_path = "books/frankenstein.txt"
    book_contents = get_book_text(book_path)
    num_words = count_words(book_contents)
    print(f"Found {num_words} total words")
    return

main()