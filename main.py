import sys

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
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {amount} total words")
    print("--------- Character Count -------")
    for dict_item in sorted_list:
        if dict_item["char"].isalpha():
            print(f"{dict_item["char"]}: {dict_item["num"]}")
    print("============= END ===============")




def main():
   if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
   else:
        filepath = sys.argv[1]
        amount = word_count(filepath)
        characters = character_count(filepath)
        list_dict = create_dict(characters)
        sorted_list = sort_by_high(list_dict)
        print_report(amount,sorted_list)

    

main()

   
