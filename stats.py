def word_count(filepath):
    with open(filepath) as f:
        return len(f.read().split())


def character_count(filepath):
    with open(filepath) as f:
        text = f.read().lower()
        char_count = {}
        for i in text:
            if i in char_count:
                    char_count[i] += 1
            else:
                    char_count[i] = 1
    return char_count

def create_dict(input_dict):
     output_dict = []
     for key in input_dict:
          output_dict.append ({"char": key, "num": input_dict[key]})
     return output_dict
     
def sort_by_high(input_dict):
     def get_num(char_count):
          return char_count["num"]
     input_dict.sort(key=get_num, reverse=True)
     return input_dict

     
    
             




