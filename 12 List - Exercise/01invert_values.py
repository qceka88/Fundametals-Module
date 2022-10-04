input_numbers = list(map(int, input().split()))

inverted=[]

for number in input_numbers:
    inverted.append(-number)

print(inverted)



#################################### TASK CONDITION ############################
"""
                            1.	Invert Values
Write a program that receives a single string containing positive and 
negative numbers separated by a single space. Print a list containing the opposite of each number.


____________________________________________________________________________________________
Example_01

Input
1 2 -3 -3 5

Output
[-1, -2, 3, 3, -5]


____________________________________________________________________________________________
Example_02

Input
-4 0 2 57 -101

Output
[4, 0, -2, -57, 101]

"""
