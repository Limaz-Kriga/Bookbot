from stats import word_count
from stats import character_count

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    filepath = "./books/frankenstein.txt"
   # contents = get_book_text(filepath)
    amount = word_count(filepath)
    characters = character_count(filepath)
   # print(contents)
    print(f"{amount} words found in the document")
    print(characters)
    


main()

   
