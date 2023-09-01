# Simple Encryption - Decryption code

Program to encrypt and then another to decrypt some text.

Input some text and a numeric value key, text will be shifted using that key value using the Unicode table, with a loop for uppercase, lowercase or numeric values, it will also change spaces into ¶, anything else (symbols and other special characters) will be left as in the original text.

## Second Version Mark 2 (MKII files)

Made it so user has to input a 3 digit key code, then the programs encrypts the message 3 times using this digits, the first time it uses the first digit to shift each character using that value, the second time it uses the second digit to shift each character using that value*2, and the the third time it uses the third digit to shift each character using that value*3, as the first version the shift is still done using unicode table and still looping between uppercase, lowercase and numeric values, spaces are still ¶, anything else is neverchanged.
