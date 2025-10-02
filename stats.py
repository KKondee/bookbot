
def count_words(text):
    return len(text.split())

def character_counter(book):
    book = book.lower()
    counter = {}
    for letter in set(book):
        counter[letter] = book.count(letter)
    return counter

def sort_character_count(char_dict):
    return char_dict["num"]
    
