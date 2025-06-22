from stats import word_count
from stats import character_count
from stats import create_dict
from stats import sort_by_high

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def print_report(amount, sorted_list):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {amount} total words")
    print("--------- Character Count -------")
    for dict_item in sorted_list:
        if dict_item["char"].isalpha():
            print(f"{dict_item["char"]}: {dict_item["num"]}")
    print("============= END ===============")




def main():
    filepath = "./books/frankenstein.txt"
   # contents = get_book_text(filepath)
    amount = word_count(filepath)
    characters = character_count(filepath)
    list_dict = create_dict(characters)
    sorted_list = sort_by_high(list_dict)
    print_report(amount,sorted_list)
   # print(contents)
   # print(f"{amount} words found in the document")
   # print(characters)
    

main()

   
