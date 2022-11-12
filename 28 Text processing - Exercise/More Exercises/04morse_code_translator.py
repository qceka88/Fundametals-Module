class Translator:

    def __init__(self, message_list, english_dict):
        self.message_list = message_list
        self.english_dict = english_dict

    def construct_new_word(self, some_word):
        revealed_word = ''
        morse_to_english = {value: key for key, value in self.english_dict.items()}
        for letter in some_word.split():
            revealed_word += morse_to_english[letter]
        return revealed_word

    def decrypting(self):
        revealed_message = ''
        for word in self.message_list:
            revealed_message += self.construct_new_word(word) + ' '
        return revealed_message

    def __repr__(self):
        new_message = self.decrypting()
        return f'{new_message}'


english_to_morse = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
                    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}

morse_message = input().split(' | ')

translated_message = Translator(morse_message, english_to_morse)

print(translated_message)

#################################### TASK CONDITION ############################
"""
                       4.	Morse Code Translator
Write a program that translates messages from Morse code to English (capital letters). 
Use this page to help you (without the numbers). The words will be separated by a space (' '). Each word is separated by a ' | '.
Print the found words on one line, separated by a space.


____________________________________________________________________________________________
Example_01

Input
.. | -- .- -.. . |  -.-- --- ..- | .-- .-. .. - . | .- | .-.. --- -. --. | -.-. --- -.. .

Output
I MADE YOU WRITE A LONG CODE


____________________________________________________________________________________________
Example_02

Input
.. | .... --- .--. . | -.-- --- ..- | .- .-. . | -. --- - | -- .- -..

Output
I HOPE YOU ARE NOT MAD

"""
