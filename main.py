from stats import get_num_words
from stats import get_num_chars
from stats import get_sorted_list_num_chars

def get_book_text(book_path):

    with open(book_path) as f:
        book_contents = f.read()

    return book_contents

def main():
    book_path = "books/frankenstein.txt"
    book_contents = get_book_text(book_path)
    num_words = get_num_words(book_contents)
    num_chars = get_num_chars(book_contents)
    sorted_list_num_chars = get_sorted_list_num_chars(num_chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_list_num_chars:
        if item["char"].isalpha() == True:
            print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")
    return

main()