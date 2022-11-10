class Repeating:

    def __init__(self, word):
        self.word = word

    def repeating(self):
        repeated = self.word * len(self.word)
        return repeated

    def __repr__(self):
        return f'{self.repeating()}'

input_line = input().split()

for word in input_line:
    repeat_word = Repeating(word)
    print(repeat_word,end='')




#################################### TASK CONDITION ############################
"""
                             2.	Repeat Strings
Write a program that reads a sequence of strings, 
separated by a single space. Each string should be repeated N times, 
where N is the length of the string. Print the final strings concatenated into one string.

____________________________________________________________________________________________
Example_01

Input
hi abc add

Output
hihiabcabcabcaddaddadd

____________________________________________________________________________________________
Example_02

Input
work

Output
workworkworkwork

____________________________________________________________________________________________
Example_03

Input
ball

Output
ballballballball

"""
