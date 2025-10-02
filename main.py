
def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents

def main():
    book_path = "books/frankenstein.txt"
    book = get_book_text(book_path)
    print(book)

main()
