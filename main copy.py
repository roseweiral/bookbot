def main():
    book_path = "books/frankenstein.txt" # Book to be processed
    text = get_book_text(book_path) # Read the Book defined in book path variable using the Function get_book_text
    num_words = get_num_words(text) #  Counts the number of words in the text useing the Function get_num_words
    charecter = count_characters(text) # counts the number of times each charcter is used in every word of text - using Function count_charecters
    ordered_char_count = count_characters(charecter) # orders the output of the count_charecters to rank by most used letter using function order_charecter_count.
    print(f"{num_words} words found in the document")
    print(f"There are {charecter}")
    print("-----------------")    
    print(order_charecter_count(charecter))

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

def order_charecter_count(char_count):
    #Initialize empty list to store result.
    print("*******************************************")
    print("CREATE EMPTY LIST")
    ordered_char_count = []

    #Iterate through input to look for letters and then order by most used letter.
    ordered_char_count.append(char_count)
    print(ordered_char_count)
    # Return List
    return (order_charecter_count)
main()