from collections import defaultdict

def words_count(sentence):
    updated_sentence = sentence.split()
    return len(updated_sentence)

def  get_text_book(book_name):
    with open(book_name) as f:
        return f.read()
    
def count_character(text):
    char_freq = defaultdict(int)
    for char in text:
        char_freq[char.lower()] += 1
    return char_freq

def print_report(char_freq,word_count):
    print("--- Begin report of books/frankenstein.txt - --")
    print(f"{word_count} words found in the document")
    print()
    for key,value in sorted(char_freq.items()):
        if key.isalpha():
            print(f"The '{key}' character was found {value} times")
    print("--- End report ---")
    
def main():
    text_book_path = 'books/frankenstein.txt'
    text_book = get_text_book(text_book_path)
    word_count = words_count(text_book)
    total_characters = count_character(text_book)
    # print(total_characters)
    print_report(total_characters,word_count)
   
    
main()
