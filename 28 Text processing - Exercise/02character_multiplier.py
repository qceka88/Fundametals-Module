class Multiplier:

    def __init__(self, first, second):
        self.first = first
        self.second = second

    def lengthening(self):
        if len(self.first) > len(self.second):
            return self.second
        elif len(self.second) > len(self.first):
            return self.first
        else:
            return self.first

    def calculating(self):
        summed = 0
        for index in range(len(self.lengthening())):
            summed += ord(self.first[index]) * ord(self.second[index])
        if self.second == self.lengthening():
            summed += sum(ord(self.first[i]) for i in range(len(self.second), len(self.first)))
        if self.first == self.lengthening():
            summed += sum(ord(self.second[i]) for i in range(len(self.first), len(self.second)))
        return f'{summed}'


first_string, second_string = input().split()

multiplier = Multiplier(first_string, second_string)

print(multiplier.calculating())





#################################### TASK CONDITION ############################
"""
                       2.	 Character Multiplier
Create a program that receives two strings on a single line separated by a single space. 
Then, it prints the sum of their multiplied character codes as follows: 
multiply str1[0] with str2[0] and add the result to the total sum, 
then continue with the next two characters. If one of the strings is longer than the other, 
add the remaining character codes to the total sum without multiplication.


____________________________________________________________________________________________
Example_01

Input
George Peter

Output
52114


____________________________________________________________________________________________
Example_02

Input
123 522

Output
7647


____________________________________________________________________________________________
Example_03

Input
a aaaa

Output
9700

"""
