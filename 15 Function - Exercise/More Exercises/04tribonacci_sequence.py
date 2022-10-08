def tribonacci(input_number):
    tribonacci_initial = [0, 0, 1]

    for number in range(input_number - 1):
        new_number = tribonacci_initial[-1] + tribonacci_initial[-2] + tribonacci_initial[-3]
        tribonacci_initial.append(new_number)
    return tribonacci_initial[2:len(tribonacci_initial)]


number = int(input())
tribonacci_result = tribonacci(number)
print(*tribonacci_result)




#################################### TASK CONDITION ############################
"""
                       4.	Tribonacci Sequence
In the Tribonacci sequence, every number is formed by the sum of the previous 3.
Write a function that prints numbers from the Tribonacci sequence on one line 
separated by a single space, starting from 1. 
You will receive a positive integer number as input.


____________________________________________________________________________________________
Example_01

Input
4

Output
1 1 2 4


____________________________________________________________________________________________
Example_02

Input
8

Output
1 1 2 4 7 13 24 44

"""
