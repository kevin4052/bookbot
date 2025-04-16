import sys
from stats import get_num_words
from stats import get_char_list

def main():
    argv = sys.argv
    if len(argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        return
    # Check if the file exists
    path_to_file = argv[1]
    try:
        with open(path_to_file) as f:
            pass
    except FileNotFoundError:
        print(f"File not found: {path_to_file}")
        return
    

    with open(path_to_file) as f:
        file_contents = f.read()
        word_count = get_num_words(file_contents)
        char_list = get_char_list(file_contents)
        generateReport(path_to_file, word_count, char_list) 
        


def generateReport(file_path, word_count, char_count):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print(f"----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print(f"--------- Character Count -------")
    for char in char_count:
        print(f"'{char['name']}: {char['count']}'")
    print("============= END ===============")

main()
