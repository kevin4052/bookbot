def main():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()
        word_count = countWords(file_contents)
        char_list = countChar(file_contents)
        generateReport(path_to_file, word_count, char_list) 
        
def countWords(text):
    return len(text.split())

def countChar(text):
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

def sort_on(dict):
    return dict["count"]

def generateReport(file_path, word_count, char_count):
    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count} words found in the document \n")
    for char in char_count:
        print(f"The '{char['name']}' character was found {char['count']} times")
    print("--- End report ---")

main()
