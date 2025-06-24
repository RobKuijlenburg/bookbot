from stats import count_words, count_lowercase_letters, sort_dict 
from sys import argv, exit as sys_exit

def get_book_text(file_path):
    """
    Reads the content of a book from a text file.

    Args:
        file_path (str): The path to the text file containing the book.

    Returns:
        str: The content of the book as a string.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        file_content = file.read()
        return file_content


def main():
    args = argv
    if len(args) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys_exit(1)
    book_path = args[1]
    book_text = get_book_text(book_path)

    word_count = count_words(book_text)
    letter_count = count_lowercase_letters(book_text)

    sorted = sort_dict(letter_count)
    print('============ BOOKBOT ============')
    print(f"Analyzing book found at {book_path}...")
    print('----------- Word Count ----------')
    print(f'Found {word_count} total words')
    print('--------- Character Count -------')
    for item in sorted: 
        print(f"{item['char']}: {item['count']}")
    print('============= END ===============')

main()
