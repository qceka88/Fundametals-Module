initial_numbers = list(map(int, input().split(', ')))

for number in initial_numbers:
    if number == 0:
        initial_numbers.remove(number)
        initial_numbers.append(number)

print(initial_numbers)

#################################### TASK CONDITION ############################
"""
                       1.	Zeros to Back
Write a program that receives a single string (integers separated by a comma and space ", "), 
finds all the zeros, and moves them to the back without messing up the other elements. 
Print the resulting integer list.


____________________________________________________________________________________________
Example_01

Input
1, 0, 1, 2, 0, 1, 3

Output
[1, 1, 2, 1, 3, 0, 0]


____________________________________________________________________________________________
Example_02

Input
0, 5, 0, 4, 0, 0, 5

Output
[5, 4, 5, 0, 0, 0, 0]

"""
