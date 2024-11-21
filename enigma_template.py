# enigma.py
# description: a simple rotational ciphertext program that can create
# custom encoded messages, as well as encode and decode from file.
# author: Jaidyn Beagan
# created: 11.18.2024
# last update:  11.18.2024

import random

# we'll be using this string for the majority of our translations
alphabet = "abcdefghijklmnopqrstuvwxyz"

# user inputs a message and selects a key (or random), the message is then translated using the cipher
def encode_message():
    msg = input("Enter a message to encode:  ")
    cp1 = int(input("Enter the cipher key:  "))
    o1 = " "
    for char in msg.lower():
        if char == " ":
            o1 += char
        else:
            index1 = alphabet.find(char)
            new_index1 = (index1 + cp1) % len(alphabet)
            o1 += alphabet[new_index1]
    print('Encoded Message:', o1)
    pass

# encodes a target file, similarly to encode_message, except now targeting a filename
def encode_file():
    # my goal here is to figure out how to pull the text from the file and change that into a variable
    file1 = input(f"Enter a file name to encode \n(choose 1.txt, 2.txt, or 3.txt) :\n                                  ")
    cp2 = int(input("Enter the cipher key:  "))
    o2 = " "
    if file1 == "1.txt":
        f = open(file1, "r")
        print(f"File content: {f.read()}")
        f.close()
        for char in file1:
            if char == " ":
                o2 += char
            else:
                index2 = alphabet.find(char)
                new_index2 = (index2 + cp2) % len(alphabet)
                o2 += alphabet[new_index2]
    print('Encoded Message:', o2)
    pass


# decodes target file using a user-specified key. If key is unknown, a keypress should
# call decode_unknown_key()
def decode_file():
    pass

# runs if the key is unknown. If this is true, print out all possible decoding combinations.
def decode_unknown_key(filename):
   pass


# main method declaration
def main():
    while True:
        print(f"Welcome to the Enigma Machine!\n"
              f"Please select an option:\n"
              f"[1]: Encode a custom message.\n"
              f"[2]: Encode file.\n"
              f"[3]: Decode file.\n"
              f"[4]: Exit.")

        selection = input("Choose an option:")

        if selection == "1":
            encode_message()
        elif selection == "2":
            encode_file()
        elif selection == "3":
            decode_file()
        elif selection == "4":
            print("Goodbye.")
            exit()
        else:
            print("Invalid choice. Please try again.")

# runs on program start
if __name__ == "__main__":
    main()