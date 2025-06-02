from stats import get_num_words, get_num_chars,sort_chars
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()

    return file_contents
    


def main():
    if len(sys.argv)<2:
      print("Usage: python3 main.py <path_to_book>")  
      sys.exit(1)
    sys_argv = sys.argv[1]
    
    text = get_book_text(sys_argv)
    dict = get_num_chars(text)
    total_words = get_num_words(text)
    sorted_chars = sort_chars(dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys_argv}...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    for i in sorted_chars:
        if i["char"].isalpha():
            print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")
main()