line_numbers = int(input())

my_list = []
for number in range(line_numbers):
    current_string = input()
    my_list.append(current_string)

print(my_list)




#################################### TASK CONDITION ############################
"""
                        2.	Courses
On the first line, you will receive a single number n.
On the following n lines, you will receive names of courses.
You should create a list of courses and print it.


____________________________________________________________________________________________
Example_01

Input
2
PB Python
PF Python

Output
['PB Python', 'PF Python']


____________________________________________________________________________________________
Example_02


Input
4
Front-End
C# Web
JS Core
Programming Fundamentals

Output
['Front-End', 'C# Web', 'JS Core', 'Programming Fundamentals']

"""