# enigma.py
# description: a simple rotational ciphertext program that can create
# custom encoded messages, as well as encode and decode from file.
# author: Jaidyn Beagan
# created: 11.18.2024
# last update:  11.27.2024

import random

# we'll be using this string for the majority of our translations
alphabet = "abcdefghijklmnopqrstuvwxyz"

# user inputs a message and selects a key (or random), the message is then translated using the cipher
def encode_message():
    # makes an input variable
    msg = input("Enter a message to encode:  ")
    # makes an input, integer variable
    cp1 = int(input("Enter the cipher key:  "))
    # makes a blank variable
    o1 = " "
    # makes characters in msg lowercase
    for char in msg.lower():
        # if characters have a space
        if char == " ":
            # adds characters onto the empty variable (making it a list)
            o1 += char
        else:
            # if the characters are in the alpahbet
            if char in alphabet:
                # makes a new variable of the character's placement in the alphabet
                index1 = alphabet.find(char)
                # makes a new variable of the placement plus the cipher key moduled by 26
                new_index1 = (index1 + cp1) % len(alphabet)
                # adds characters onto the empty variable
                o1 += alphabet[new_index1]
            # otherwise, add the character onto the list
            else:
                o1 += char
    print('Encoded Message:', o1)
    pass

# encodes a target file, similarly to encode_message, except now targeting a filename
def encode_file():
    # makes an input variable
    choice = input(f"Enter a file name to encode \n(choose 1.txt, 2.txt, or 3.txt) :\n                                  ")
    # makes an input, integer variable
    cp2 = int(input("Enter the cipher key:  "))
    # makes a blank variable
    o2 = " "
    if choice == "1.txt":
        # open the chosen file as f
        with open(choice) as f:
            # makes a variable of the file's content
            trying = f.read()
            # prints the files content
            print(f"File content: {trying}")
            # closes file
            f.close()
        # makes characters in the chosen file lowercase
        for char in trying.lower():
            if char == " ":
                o2 += char
            else:
                if char in alphabet:
                    index2 = alphabet.find(char)
                    new_index2 = (index2 + cp2) % len(alphabet)
                    o2 += alphabet[new_index2]
                else:
                    o2 += char
    if choice == "2.txt":
        with open(choice) as f:
            trying = f.read()
            print(f"File content: {trying}")
            f.close()
        # makes characters in the chosen file lowercase
        for char in trying.lower():
            if char == " ":
                o2 += char
            else:
                if char in alphabet:
                    index2 = alphabet.find(char)
                    new_index2 = (index2 + cp2) % len(alphabet)
                    o2 += alphabet[new_index2]
                else:
                    o2 += char
    if choice == "3.txt":
        with open(choice) as f:
            trying = f.read()
            print(f"File content: {trying}")
            f.close()
        # makes characters in the chosen file lowercase
        for char in trying.lower():
            if char == " ":
                o2 += char
            else:
                if char in alphabet:
                    index2 = alphabet.find(char)
                    new_index2 = (index2 + cp2) % len(alphabet)
                    o2 += alphabet[new_index2]
                else:
                    o2 += char
    print('Encoded Message:', o2)
    pass

# decodes target file using a user-specified key. If key is unknown, a keypress should
# call decode_unknown_key()
def decode_file():
    # makes an input variable
    yn = input("Do you know the cipher key? ")
    if yn == "no":
        # goes to the function to decode with an unknown cipher key
        decode_unknown_key()
    else:
        # makes an input variable
        choice1 = input(
            f"Enter a file name to decode \n(choose 4.txt, 5.txt, or 6.txt) :\n                                  ")
        # makes an input, integer variable
        cp3 = int(input("Enter the cipher key:  "))
        # makes a blank variable
        o3 = " "
        if choice1 == "4.txt":
            with open(choice1) as f:
                trying1 = f.read()
                print(f"File content: {trying1}")
                f.close()
            # makes characters in the chosen file lowercase
            for char in trying1.lower():
                if char == " ":
                    o3 += char
                else:
                    if char in alphabet:
                        index3 = alphabet.find(char)
                        new_index3 = (index3 - cp3) % len(alphabet)
                        o3 += alphabet[new_index3]
                    else:
                        o3 += char
        if choice1 == "5.txt":
            with open(choice1) as f:
                trying1 = f.read()
                print(f"File content: {trying1}")
                f.close()
            # makes characters in the chosen file lowercase
            for char in trying1.lower():
                if char == " ":
                    o3 += char
                else:
                    if char in alphabet:
                        index3 = alphabet.find(char)
                        new_index3 = (index3 - cp3) % len(alphabet)
                        o3 += alphabet[new_index3]
                    else:
                        o3 += char
        if choice1 == "6.txt":
            with open(choice1) as f:
                trying1 = f.read()
                print(f"File content: {trying1}")
                f.close()
            # makes characters in the chosen file lowercase
            for char in trying1.lower():
                if char == " ":
                    o3 += char
                else:
                    if char in alphabet:
                        index3 = alphabet.find(char)
                        new_index3 = (index3 - cp3) % len(alphabet)
                        o3 += alphabet[new_index3]
                    else:
                        o3 += char
        print('Decoded Message:', o3)
    pass

# runs if the key is unknown. If this is true, print out all possible decoding combinations.
def decode_unknown_key():
    # makes an input variable
    choice2 = input(
        f"Enter a file name to decode \n(choose 4.txt, 5.txt, or 6.txt) :\n                                  ")
    if choice2 == "4.txt":
        with open(choice2) as f:
            trying2 = f.read()
            print(f"File content: {trying2}")
            f.close()
        for key in range(0, 26, 1):
            # makes a blank variable
            o4 = " "
            # makes characters in the chosen file lowercase
            for char in trying2.lower():
                if char in alphabet:
                    index4 = alphabet.find(char)
                    new_index4 = (index4 + key) % len(alphabet)
                    o4 += alphabet[new_index4]
                else:
                    o4 += char
            print('Decoded Message:', o4)
    if choice2 == "5.txt":
        with open(choice2) as f:
            trying2 = f.read()
            print(f"File content: {trying2}")
            f.close()
        for key in range(0, 26, 1):
            # makes a blank variable
            o4 = " "
            # makes characters in the chosen file lowercase
            for char in trying2.lower():
                if char in alphabet:
                    index4 = alphabet.find(char)
                    new_index4 = (index4 + key) % len(alphabet)
                    o4 += alphabet[new_index4]
                else:
                    o4 += char
            print('Decoded Message:', o4)
    if choice2 == "6.txt":
        with open(choice2) as f:
            trying2 = f.read()
            print(f"File content: {trying2}")
            f.close()
        for key in range(0, 26, 1):
            # makes a blank variable
            o4 = " "
            # makes characters in the chosen file lowercase
            for char in trying2.lower():
                if char in alphabet:
                    index4 = alphabet.find(char)
                    new_index4 = (index4 + key) % len(alphabet)
                    o4 += alphabet[new_index4]
                else:
                    o4 += char
            print('Decoded Message:', o4)
    pass
# runs if the key is unknown. If this is true, print out all possible decoding combinations.
def decode_msg():
    # makes an input variable
    msg1 = input("Enter a message to decode:  ")
    for key1 in range(0, 26, 1):
        # makes a blank variable
        o5 = " "
        # makes characters in the msg lowercase
        for char in msg1.lower():
            if char in alphabet:
                index5 = alphabet.find(char)
                new_index5 = (index5 + key1) % len(alphabet)
                o5 += alphabet[new_index5]
            else:
                o5 += char
        print('Decoded Message:', o5)
    pass

# main method declaration
def main():
    while True:
        print(f"Welcome to the Enigma Machine!\n"
              f"Please select an option:\n"
              f"[1]: Encode a custom message.\n"
              f"[2]: Decode a custom message with an unknown key.\n"
              f"[3]: Encode file.\n"
              f"[4]: Decode file.\n"
              f"[5]: Decode file with an unknown key.\n"
              f"[6]: Exit.")

        selection = input("Choose an option:")

        if selection == "1":
            encode_message()
        elif selection == "2":
            decode_msg()
        elif selection == "3":
            encode_file()
        elif selection == "4":
            decode_file()
        elif selection == "5":
            decode_unknown_key()
        elif selection == "6":
            print("Goodbye.")
            exit()
        else:
            print("Invalid choice. Please try again.")

# runs on program start
if __name__ == "__main__":
    main()