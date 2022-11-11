class Reverse:

    def __init__(self, word):
        self.word = word
        self.reversed_word = ''

    def reversing_word(self):
        self.reversed_word = self.word[::-1]
        return self.reversed_word

    def __repr__(self):
        return f"{self.word} = {self.reversing_word()}"


while True:
    input_word = input()
    if input_word == 'end':
        break
    reversing = Reverse(input_word)
    print(reversing)




#################################### TASK CONDITION ############################
"""
                           1.	Reverse Strings
You will be given strings on separate lines until you receive an "end" command. 
Write a program that reverses strings and prints each pair on a separate line in the format "{word} = {reversed_word}".


____________________________________________________________________________________________
Example_01

Input
helLo
Softuni
bottle
end

Output
helLo = oLleh
Softuni = inutfoS
bottle = elttob


____________________________________________________________________________________________
Example_02

Input
Dog
caT
chAir
end

Output
Dog = goD
caT = Tac
chAir = riAhc

"""
