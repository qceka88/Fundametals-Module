import re


class Extract:

    def __init__(self, data):
        self.data = data

    def regex_action(self):
        match = re.findall(r'\d+', self.data)
        return match


input_line = input()

numbers = []

while input_line:
    result = Extract(input_line)
    numbers.extend(result.regex_action())
    input_line = input()

print(*numbers)

#################################### TASK CONDITION ############################
"""

                             1.	Capture the Numbers
Write a program that receives strings on different lines and extracts only the numbers.
Print all extracted numbers on a single line, separated by a single space.

____________________________________________________________________________________________
Example_01

Input
The300
What is that?
I think it's the 3rd movie 
Let's watch it at 22:45	

Output
300 3 22 45

____________________________________________________________________________________________
Example_02

Input
123a456
789b987
654c321
0	

Output
123 456 789 987 654 321 0

____________________________________________________________________________________________
Example_03

Input
Let's go11!!!11!
Okey!1!

Output
11 11 1

"""
