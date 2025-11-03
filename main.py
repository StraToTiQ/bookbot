def get_book_text(book_path):

    with open(book_path) as f:
        book_contents = f.read()

    return book_contents

def main():
    book_path = "books/frankenstein.txt"
    book_contents = get_book_text(book_path)
    print(book_contents)
    return

main()