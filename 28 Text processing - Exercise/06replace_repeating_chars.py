class Replacing:

    def __init__(self, string):
        self.string = string

    def clearing(self):
        new_text = ''
        last_symbol = ''
        for symbol in self.string:
            if last_symbol != symbol:
                last_symbol = symbol
                new_text += last_symbol
        return new_text

    def __repr__(self):
        return f'{self.clearing()}'


single_string = input()

new_string = Replacing(single_string)

print(new_string)





#################################### TASK CONDITION ############################
"""
                  6.	 Replace Repeating Chars
Write a program that reads a string from the console and replaces any 
sequence of the same letters with a single corresponding letter.


____________________________________________________________________________________________
Example_01

Input
aaaaabbbbbcdddeeeedssaa

Output
abcdedsa


____________________________________________________________________________________________
Example_02

Input
qqqwerqwecccwd

Output
qwerqwecwd

"""
