# Encryption - Decryption Program

Making a program to encrypt and decrypt text and evolving it as I advance my python knowledge.

## First version

Two separate programs to encrypt and decrypt. User inputs some text and a numeric value key, text will be shifted using that key value using the Unicode table, with a loop for uppercase, lowercase or numeric values, it will also change spaces into ¶, anything else (symbols and other special characters) will be left as in the original text.

## Second Version Mark 2 (MKII files)

Made it so user has to input a 3 digit key code, then the program encrypts the message 3 times using these digits, the first time it uses the first digit to shift each character using that value, the second time it uses the second digit to shift each character using that value x2, and the the third time it uses the third digit to shift each character using that value x3. As in the first version the shifts are still done using Unicode table and still looping between uppercase, lowercase and numeric values, spaces are still ¶, anything else is not changed.

## Third Version Mark 3 (MKIII file)

Reduced to a single program to give a choice between encrypting or decrypting, also simplified the code using 'def' functions. It still works as in Mark 2 on how it encrypts, but added several loops to include spaces and all basic latin special characters to also be shifted using the unicode table. Any other special characters (latin supplement, extended or other languages) should remain the same.

### Roadmap:
- #### WIP Fourth Version Mark 4:
  Working on making the program not require specifically a 3 digit key, but instead let the user input any lenght key they want, and the program should encrypt the text following the same logic as before of all text's characters being shifted in order for each   
  digit in the key by the value of the digit multiplied to its position, using its corresponding unicode table values.

- #### Probably Final Version Mark V:
  Thinking on letting the key be any type of character and if it's not a number making the program convert it to an integer value by using their unicode ord value. May include shifting for other Lating characters and maybe most common symbols from other languages.

