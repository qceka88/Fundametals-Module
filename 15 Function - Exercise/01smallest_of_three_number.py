def smallest(one, two, three):
    min_number = [one, two, three]
    return min(min_number)


first_number = int(input())
second_number = int(input())
third_number = int(input())

result = smallest(first_number, second_number, third_number)

print(result)



#################################### TASK CONDITION ############################
"""
                  1. Smallest of Three Numbers
Write a function that receives three integer numbers and returns the smallest.
Print the result on the console. Use an appropriate name for the function.


____________________________________________________________________________________________
Example_01

Input
2
5
3

Output
2


____________________________________________________________________________________________
Example_02

Input
600
342
123

Output
123


____________________________________________________________________________________________
Example_03

Input
25
21
44
4

Output
4

"""
