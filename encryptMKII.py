plain_text = input("What is the message?: ")
key_input = True
while key_input == True:
    shift_key = int(input("Enter a 3 digit key: "))
    shift_key = str(shift_key)
    if len(shift_key) == 3:
        key_input = False
        shift_key = int(shift_key)
    else:
        print("Invalid key, enter a 3 digit key: ")
        continue

cipher_text = ''

    
for letter in plain_text:
    if letter == " ":
        cipher_text += "¶"
    elif letter.isupper():
        char_position = ord(letter)
        new_position = ((char_position + (int(str(shift_key)[0])) - 65) % 26) + 65
        new_letter = chr(new_position)
        cipher_text += new_letter
    elif letter.islower():
        char_position = ord(letter)
        new_position = ((char_position + (int(str(shift_key)[0])) - 97) % 26) + 97
        new_letter = chr(new_position)
        cipher_text += new_letter
    elif letter.isnumeric():
        char_position = ord(letter)
        new_position = ((char_position + (int(str(shift_key)[0])) - 48) % 10) + 48
        new_letter = chr(new_position)
        cipher_text += new_letter
    else:
        cipher_text += letter


cipher_text2 = ''

for letter in cipher_text:
    if letter == " ":
        cipher_text2 += "¶"
    elif letter.isupper():
        char_position2 = ord(letter)
        new_position2 = ((char_position2 + (int(str(shift_key)[1]))*2 - 65) % 26) + 65
        new_letter2 = chr(new_position2)
        cipher_text2 += new_letter2
    elif letter.islower():
        char_position2 = ord(letter)
        new_position2 = ((char_position2 + (int(str(shift_key)[1]))*2 - 97) % 26) + 97
        #print(new_position2)
        new_letter2 = chr(new_position2)
        #print(new_letter2)
        cipher_text2 += new_letter2
    elif letter.isnumeric():
        char_position2 = ord(letter)
        new_position2 = ((char_position2 + (int(str(shift_key)[1]))*2 - 48) % 10) + 48
        new_letter2 = chr(new_position2)
        cipher_text2 += new_letter2
    else:
        cipher_text2 += letter


cipher_text3 = ''

for letter in cipher_text2:
    if letter == " ":
        cipher_text3 += "¶"
    elif letter.isupper():
        char_position3 = ord(letter)
        new_position3 = ((char_position3 + (int(str(shift_key)[2]))*3 - 65) % 26) + 65
        new_letter3 = chr(new_position3)
        cipher_text3 += new_letter3
    elif letter.islower():
        char_position3 = ord(letter)
        new_position3 = ((char_position3 + (int(str(shift_key)[2]))*3 - 97) % 26) + 97
        new_letter3 = chr(new_position3)
        cipher_text3 += new_letter3
    elif letter.isnumeric():
        char_position3 = ord(letter)
        new_position3 = ((char_position3 + (int(str(shift_key)[2]))*3 - 48) % 10) + 48
        new_letter3 = chr(new_position3)
        cipher_text3 += new_letter3
    else:
        cipher_text3 += letter


print(cipher_text3)