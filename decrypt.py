plain_text = input("What is the message?: ")
shift_key = int(input("What is the key?: "))

cipher_text = ''

    
for letter in plain_text:
    if letter == "¶":
        cipher_text += " "
    elif letter.isupper():
        char_position = ord(letter)
        new_position = ((char_position - shift_key - 65) % 26) + 65
        new_letter = chr(new_position)
        cipher_text += new_letter
    elif letter.islower():
        char_position = ord(letter)
        new_position = ((char_position - shift_key - 97) % 26) + 97
        new_letter = chr(new_position)
        cipher_text += new_letter
    elif letter.isnumeric():
        char_position = ord(letter)
        new_position = ((char_position - shift_key - 48) % 10) + 48
        new_letter = chr(new_position)
        cipher_text += new_letter
    else:
        cipher_text += letter

print(cipher_text)