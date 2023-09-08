def shift_char(char, key):
    if 'A' <= char <= 'Z':
        return chr(((ord(char) - ord('A') + key) % 26) + ord('A'))
    elif 'a' <= char <= 'z':
        return chr(((ord(char) - ord('a') + key) % 26) + ord('a'))
    elif '0' <= char <= '9':
        return chr(((ord(char) - ord('0') + key) % 10) + ord('0'))
    elif ' ' <= char <= '/':
        return chr(((ord(char) - ord(' ') + key) % 16) + ord(' '))
    elif ':' <= char <= '@':
        return chr(((ord(char) - ord(':') + key) % 7) + ord(':'))
    elif '[' <= char <= '`':
        return chr(((ord(char) - ord('[') + key) % 6) + ord('['))
    elif '{' <= char <= '~':
        return chr(((ord(char) - ord('{') + key) % 6) + ord('{'))
    else:
        return char

def encrypt(text, key):
    encrypted_text = ""
    key_digits = [int(digit) for digit in str(key)]
    key_digit_index = 0
    for char in text:
        digit = key_digits[key_digit_index]
        encrypted_text += shift_char(char, digit)
        key_digit_index = (key_digit_index + 1) % len(key_digits)
    return encrypted_text

def decrypt(encrypted_text, key):
    decrypted_text = ""
    key_digits = [int(digit) for digit in str(key)]
    key_digit_index = 0
    for char in encrypted_text:
        digit = key_digits[key_digit_index]
        decrypted_text += shift_char(char, -digit)
        key_digit_index = (key_digit_index + 1) % len(key_digits)
    return decrypted_text


choice = input("Choose 'E' to encrypt or 'D' to decrypt: ")

if choice == 'E' or choice == 'e':
    text = input("Enter the text to encrypt: ")
    key = int(input("Enter the encryption key (a three-digit integer): "))
    if 100 <= key <= 999:
        encrypted_text = encrypt(text, key)
        print("Encrypted Text:", encrypted_text)
    else:
        print("Please enter a three-digit key.")

elif choice == 'D' or choice == 'd':
    encrypted_text = input("Enter the encrypted text: ")
    key = int(input("Enter the decryption key (a three-digit integer): "))
    if 100 <= key <= 999:
        decrypted_text = decrypt(encrypted_text, key)
        print("Decrypted Text:", decrypted_text)
    else:
        print("Please enter a three-digit key.")
        
else:
    print("Invalid choice. Please choose 'E' for encryption or 'D' for decryption.")
