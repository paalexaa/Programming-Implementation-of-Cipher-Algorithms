import string
# import numpy as np
import math
# import utils

def caesar_cipher(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + key
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

def vigenere(text, key):
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    plaintext_int = [ord(i) for i in text]
    ciphertext = ''
    for i in range(len(plaintext_int)):
        value = (plaintext_int[i] + key_as_int[i % key_length]) % 26
        ciphertext += chr(value + 65)
    return ciphertext

def affine(text, keyA, keyB):
    key = [keyA, keyB]
    return ''.join([ chr((( key[0] * (ord(t) - ord('A')) + key[1]) % 26) + ord('A')) for t in text.upper().replace(' ', '') ])

def substitution_cipher(text, key):
    all_letters = string.ascii_letters
    dict1 = {}

    for i in range(len(all_letters)):
        dict1[all_letters[i]] = all_letters[(i + key) % len(all_letters)]

    cipher_txt = []
    for char in text:
        if char in all_letters:
            temp = dict1[char]
            cipher_txt.append(temp)
        else:
            temp = char
            cipher_txt.append(temp)

    cipher_txt = "".join(cipher_txt)

    return cipher_txt

def otp(text, key):
    if len(text) != len(key):
        print("Error: Please enter another key as long as the size of the message.")
    else:
        cipherText = ""
        cipher = []

        for i in range(len(key)):
            cipher.append(ord(text[i]) - ord('A') + ord(key[i]) - ord('A'))

        for i in range(len(key)):
            if cipher[i] > 25:
                cipher[i] = cipher[i] - 26

        for i in range(len(key)):
            x = cipher[i] + ord('A')
            cipherText += chr(x)

        return cipherText

def rsa(text, modulus, key):

    ciphertext = pow(text, key, modulus)
    return ciphertext

def main():
    while True:
        print("Menu:")
        print("1. Caesar Cipher")
        print("2. Vigenere")
        print("3. Affine")
        print("4. Substitution Cipher")
        print("5. OTP")
        print("6. RSA")
        print("7. Exit")

        choice = input("Enter your choice (1/2/3/4/5/6/7): ")

        if choice == '1':
            text = input("Enter text to encrypt: ")
            try:
                key = int(input("Enter the encryption key (0-25): "))
                print("Encrypted text:", caesar_cipher(text, key))
                break
            except ValueError:
                print("Invalid input for the encryption key. Please enter an integer.")
        elif choice == '2':
            text = input("Enter text to encrypt: ")
            try:
                key = input("Enter the encryption key A-Z or a-z: ")
                print("Encrypted text:", vigenere(text, key))
                break
            except ValueError:
                print("Invalid input for the encryption key. Please enter another key.")
        elif choice == '3':
            text = input("Enter text to encrypt: ")
            try:
                keyA = int(input("Enter the encryption key_1 (0-25): "))
                keyB = int(input("Enter the encryption key_2: "))
                print("Encrypted text:", affine(text, keyA, keyB))
                break
            except ValueError:
                print("Invalid input for the encryption key. Please enter an integer.")
        elif choice == '4':
            text = input("Enter text to encrypt: ")
            try:
                key = int(input("Enter the encryption key (0-25): "))
                print("Encrypted text:", substitution_cipher(text, key))
                break
            except ValueError:
                print("Invalid input for the encryption key. Please enter an integer.")
        elif choice == '5':
            text = input("Enter text to encrypt: ")
            try:
                key = input("Enter the encryption key: ")
                print("Encrypted text:", otp(text.upper(), key.upper()))
                break
            except ValueError:
                print("Invalid input for the encryption key. Please enter another key.")
        elif choice == '6':
            text = int(input("Enter number to encrypt: "))
            try:
                modulus = int(input("Enter the encryption modulus: "))
                public_key = int(input("Enter the encryption public key: "))
                print("Encrypted text:", rsa(text, modulus, public_key))
                break
            except ValueError:
                print("Invalid input for the encryption key. Please enter an integer.")
        elif choice == '7':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()