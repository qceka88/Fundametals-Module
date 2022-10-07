def add_and_subtract(one, two, three):
    sum_of_numbers = sum_numbers(one, two)
    substract_of_number = subtract(sum_of_numbers, three)
    return substract_of_number


def subtract(sum, three):
    substraction = sum - three
    return substraction


def sum_numbers(one, two):
    sum = one + two
    return sum


first_number = int(input())
second_number = int(input())
third_number = int(input())

result = add_and_subtract(first_number, second_number, third_number)
print(result)



#################################### TASK CONDITION ############################
"""
                          2. Add and Subtract
You will receive three integer numbers. 
Write functions named:
•	sum_numbers() that returns the sum of the first two integers
•	subtract() that returns the difference between the 
returned result of the first function and the third integer
Wrap the two functions in a function named add_and_subtract() 
which will receive the three numbers as parameters. Print the result of the subtract() function on the console.


____________________________________________________________________________________________
Example_01

Input
23
6
10

Output
19


____________________________________________________________________________________________
Example_02

Input
1
17
30

Output
-12


____________________________________________________________________________________________
Example_03

Input
42
58
100

Output
0

"""
