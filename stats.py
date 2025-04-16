def sort_on(dict):
    return dict["count"]

def get_num_words(text):
    return len(text.split())

def get_char_list(text):
    freq = {}
    for char in text.lower():
        if not char.isalpha():
            continue
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    char_list = []
    for char in freq:
        char_list.append({
            "name": char,
            "count": freq[char]
        })

    char_list.sort(reverse=True, key=sort_on)
    return char_list

