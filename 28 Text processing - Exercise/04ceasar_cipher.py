class Hiding:

    def __init__(self, text):
        self.text = text

    def encryption(self):
        hidden = ''.join(chr(ord(symbol) + 3) for symbol in self.text)
        return hidden

    def __repr__(self):
        return self.encryption()


message = input()

hidden_message = Hiding(message)

print(hidden_message)







#################################### TASK CONDITION ############################
"""
                      4.	 Caesar Cipher
Write a program that returns an encrypted version of the same text. 
Encrypt the text by replacing each character with the corresponding character 
three positions forward in the ASCII table. For example, A would be replaced 
with D, B would become E, and so on. Print the encrypted text.


____________________________________________________________________________________________
Example_01

Input
Programming is cool!

Output
Surjudpplqj#lv#frro$


____________________________________________________________________________________________
Example_02

Input
One year has 365 days.

Output
Rqh#|hdu#kdv#698#gd|v1

"""

