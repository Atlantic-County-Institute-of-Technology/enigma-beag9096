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
    choice = input(f"Enter a file name to encode \n(choose 1.txt, 2.txt, or 3.txt) :\n                                  ")
    cp2 = int(input("Enter the cipher key:  "))
    o2 = " "
    if choice == "1.txt":
        with open(choice) as f:
            trying = f.read()
            print(f"File content: {trying}")
            f.close()
        for char in trying.lower():
            if char == " ":
                o2 += char
            else:
                index2 = alphabet.find(char)
                new_index2 = (index2 + cp2) % len(alphabet)
                o2 += alphabet[new_index2]
    if choice == "2.txt":
        with open(choice) as f:
            trying = f.read()
            print(f"File content: {trying}")
            f.close()
        for char in trying.lower():
            if char == " ":
                o2 += char
            else:
                index2 = alphabet.find(char)
                new_index2 = (index2 + cp2) % len(alphabet)
                o2 += alphabet[new_index2]
    if choice == "3.txt":
        with open(choice) as f:
            trying = f.read()
            print(f"File content: {trying}")
            f.close()
        for char in trying.lower():
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
    yn = input("Do you know the cipher key? ")
    if yn == "no":
        decode_unknown_key()
    else:
        choice1 = input(
            f"Enter a file name to decode \n(choose 4.txt, 5.txt, or 6.txt) :\n                                  ")
        cp3 = int(input("Enter the cipher key:  "))
        o3 = " "
        if choice1 == "4.txt":
            with open(choice1) as f:
                trying1 = f.read()
                print(f"File content: {trying1}")
                f.close()
            for char in trying1.lower():
                if char == " ":
                    o3 += char
                else:
                    index3 = alphabet.find(char)
                    new_index3 = (index3 - cp3) % len(alphabet)
                    o3 += alphabet[new_index3]
        if choice1 == "5.txt":
            with open(choice1) as f:
                trying1 = f.read()
                print(f"File content: {trying1}")
                f.close()
            for char in trying1.lower():
                if char == " ":
                    o3 += char
                else:
                    index3 = alphabet.find(char)
                    new_index3 = (index3 - cp3) % len(alphabet)
                    o3 += alphabet[new_index3]
        if choice1 == "6.txt":
            with open(choice1) as f:
                trying1 = f.read()
                print(f"File content: {trying1}")
                f.close()
            for char in trying1.lower():
                if char == " ":
                    o3 += char
                else:
                    index3 = alphabet.find(char)
                    new_index3 = (index3 - cp3) % len(alphabet)
                    o3 += alphabet[new_index3]
        print('Decoded Message:', o3)
    pass

# runs if the key is unknown. If this is true, print out all possible decoding combinations.
def decode_unknown_key():
    # i = range(26, 52, 1)
    # i = 26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52
    choice2 = input(
        f"Enter a file name to decode \n(choose 4.txt, 5.txt, or 6.txt) :\n                                  ")
    o4 = " "
    if choice2 == "4.txt":
        with open(choice2) as f:
            trying2 = f.read()
            print(f"File content: {trying2}")
            f.close()
        for char in trying2.lower():
            if char == " ":
                o4 += char
            else:
                index4 = alphabet.find(char)
                while i <= 52:
                    new_index4 = (index4 - i[]) % len(alphabet)
                o4 += alphabet[new_index4]
    print('Decoded Message:', o4)
    pass


# main method declaration
def main():
    while True:
        print(f"Welcome to the Enigma Machine!\n"
              f"Please select an option:\n"
              f"[1]: Encode a custom message.\n"
              f"[2]: Encode file.\n"
              f"[3]: Decode file.\n"
              f"[4]: Decode file with an unknown key.\n"
              f"[5]: Exit.")

        selection = input("Choose an option:")

        if selection == "1":
            encode_message()
        elif selection == "2":
            encode_file()
        elif selection == "3":
            decode_file()
        elif selection == "4":
            decode_unknown_key()
        elif selection == "5":
            print("Goodbye.")
            exit()
        else:
            print("Invalid choice. Please try again.")

# runs on program start
if __name__ == "__main__":
    main()