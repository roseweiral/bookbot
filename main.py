def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    charecter = count_characters(text)
    print(f"{num_words} words found in the document")
    print(f"There are {charecter}")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_characters(text):
    # Initialize an empty dictionary for character counts
    char_count = {}

    # Iterate through each character in the text
    for char in text:
        # Convert the character to lowercase
        char = char.lower()

        # If the character is already in the dictionary, increment its count
        if char in char_count:
            char_count[char] += 1
        # If the character is not in the dictionary, add it with a count of 1
        else:
            char_count[char] = 1

    # Return the dictionary of character counts
    return char_count

main()