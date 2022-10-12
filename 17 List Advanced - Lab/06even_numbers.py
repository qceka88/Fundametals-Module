numbers_list = list(map(int, input().split(', ')))
print([index for index, number in enumerate(numbers_list) if number % 2 == 0])



#################################### TASK CONDITION ############################
"""
                  6.	Even Numbers
Write a program that reads a single string with numbers 
separated by comma and space ", ". Print the indices of all even numbers.


____________________________________________________________________________________________
Example_01

Input
3, 2, 1, 5, 8

Output
[1, 4]


____________________________________________________________________________________________
Example_02

Input
2, 4, 6, 9, 10

Output
[0, 1, 2, 4]

"""
