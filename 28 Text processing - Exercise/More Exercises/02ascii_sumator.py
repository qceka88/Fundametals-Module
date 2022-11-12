class Sumator:

    def __init__(self, first, second, text):
        self.first = first
        self.second = second
        self.text = text

    def start(self):
        start_point = ord(self.first)
        return start_point

    def end(self):
        end_point = ord(self.second)
        return end_point

    def valid_character(self, symbol):
        if self.start() < ord(symbol) < self.end():
            return ord(symbol)
        return 0

    def sum_characters(self):
        total_sum = 0
        for character in self.text:
            total_sum += self.valid_character(character)
        return total_sum

    def __repr__(self):
        return f'{self.sum_characters()}'


first_character = input()
second_character = input()
string = input()

sum_of_characters = Sumator(first_character, second_character, string)

print(sum_of_characters)

#################################### TASK CONDITION ############################
"""
                              2.	ASCII Sumator
Write a program that prints the sum of all found characters between two given  
characters (their ASCII code). On each of the first two lines, you will receive a 
single character. On the last line, you get a random string. Print the sum of the 
ASCII values of all characters in the random string between the two given characters in the ASCII table.


____________________________________________________________________________________________
Example_01

Input
.
@
dsg12gr5653feee5

Output
363

Explanation
The found characters are 1, 2, 5, 6, 5, 3 and 5. 
Their ASCII sum is 49 + 50 + 53 + 54 + 53 + 51 + 53 = 363.


____________________________________________________________________________________________
Example_02

Input
?
E
@ABCEF

Output
262

"""
