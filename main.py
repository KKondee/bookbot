from stats import count_words, character_counter, sort_character_count

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents

def main():
    book_path = "books/frankenstein.txt"
    book = get_book_text(book_path)
    count = count_words(book)
    characters = character_counter(book)
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at", book_path + "...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    
    char_list = []
    for character in characters:
        if character.isalpha():
            char_list.append({"char": character, "num": characters[character]})
    char_list.sort(reverse=True, key=sort_character_count)
    for char_item in char_list:
        print(f"{char_item['char']}: {char_item['num']}")
    print("============= END ===============")
main()
