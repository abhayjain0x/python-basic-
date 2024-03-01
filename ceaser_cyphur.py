print("Have your messege encrypted or decrypted")

import os

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A']



def ceaser_cyphur():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    cipher_text = ""
    if direction == "decode":
        shift *= -1
    for char in text:
        if char in alphabets:
            position = alphabets.index(char)
            new_position = position + shift
            cipher_text += alphabets[new_position]
        else:
            cipher_text += char
    print(f"The {direction}d text is {cipher_text}")




while True:
    ceaser_cyphur()
    restart = input("Do you want to restart the program? Type 'yes' or 'no': ")
    if restart == "no":
        os.system('cls')
        break
    else:
        os.system('cls')
        continue


