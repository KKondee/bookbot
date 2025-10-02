from stats import count_words, character_counter

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents

def main():
    book_path = "books/frankenstein.txt"
    book = get_book_text(book_path)
    count = count_words(book)
    characters = character_counter(book)
    print(f"Found {count} total words")
    print(characters)

main()
