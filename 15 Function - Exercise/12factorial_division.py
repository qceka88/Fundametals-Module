from math import factorial


def factorial_number(some_number):
    return factorial(some_number)


def division_of_numbers(number_first, number_second):
    factorial01 = factorial_number(number_first)
    factorial02 = factorial_number(number_second)
    division = factorial01 / factorial02
    return division


first_number = int(input())
second_number = int(input())

result = division_of_numbers(first_number, second_number)

print(f'{result:.2f}')



#################################### TASK CONDITION ############################
"""
                            12. * Factorial Division
Write a function that receives two integer numbers. Calculate the factorial of each number. 
Divide the first result by the second and print the division formatted to the second decimal point.


____________________________________________________________________________________________
Example_01

Input
5
2

Output
60.00


____________________________________________________________________________________________
Example_02

Input
6
2

Output
360.00


Hints
•	Read more about factorial here: https://en.wikipedia.org/wiki/Factorial 

"""
