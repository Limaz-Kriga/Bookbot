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
        




