numbers = list(map(int, input().split()))
even = list(filter(lambda x: x % 2 == 0, numbers))
print(even)

#################################### TASK CONDITION ############################
"""
                     5. Even Numbers
Write a program that receives a sequence of numbers (integers)
separated by a single space. It should print a list of only the even numbers. Use filter().


____________________________________________________________________________________________
Example_01

Input
1 2 3 4

Output
[2, 4]


____________________________________________________________________________________________
Example_02

Input
1 2 3 -1 -2 -3

Output
[2, -2]

"""
