class Separating:
    def __init__(self, string):
        self.string = string
        self.alphas = []
        self.digits = []
        self.others = []

    def dividing_symbols(self):
        for symbol in self.string:
            if symbol.isdigit():
                self.digits.append(symbol)
            elif symbol.isalpha():
                self.alphas.append(symbol)
            else:
                self.others.append(symbol)
        return f'{"".join(self.digits)}\n{"".join(self.alphas)}\n{"".join(self.others)}'

    def __repr__(self):
        return f'{self.dividing_symbols()}'


input_string = input()

separated = Separating(input_string)

print(separated)




#################################### TASK CONDITION ############################
"""
                               5.	Digits, Letters, and Other
Write a program that receives a single string. On the first line, 
print all the digits found in the string, on the second – all the letters, 
and on the third – all the other characters. There will always be at least one digit, one letter, and one other character.


____________________________________________________________________________________________
Example

Input
Agd#53Dfg^&4F53

Output
53453
AgdDfgF
#^&

"""
