import sys

def main(book_path):
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    
    char_count = count_characters(text)
    #print(f"Character counts: {char_count}")
    
    sorted_characters = sort_characters_by_frequency(char_count)
    #print(f"Characters sorted by frequency: {sorted_characters}")

    for keys, values in sorted_characters:
        print(f"The {keys} charecter was found {values} times")

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path, "r") as f:
        return f.read()

def count_characters(text):
    char_count = {}
    for char in text:
        char = char.lower()
        if char.isalpha():  # Ensure we only count alphabetic characters
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count

def sort_characters_by_frequency(char_count):
    # Filter out non-alphabetic characters (this is already handled in count_characters, so this step is redundant)
    filtered_count = {char: count for char, count in char_count.items() if char.isalpha()}
    
    # Sort the dictionary by frequency in descending order
    sorted_characters = sorted(filtered_count.items(), key=lambda item: item[1], reverse=True)
    
    return sorted_characters

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <path_to_book>")
    else:
        book_path = sys.argv[1]
        main(book_path)
