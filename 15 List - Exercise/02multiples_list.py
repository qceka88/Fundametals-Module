factor = int(input())
count = int(input())

numbers_list = []
for number in range(1,count+1):
    new_number = number * factor
    numbers_list.append(new_number)

print(numbers_list)



#################################### TASK CONDITION ############################
"""
                   2.	Multiples List
Write a program that receives two numbers (factor and count). 
It should create a list with a length of the given count that contains only integer numbers,
 which are multiples of the given factor. The numbers should be only positive,
  and they should be arranged in ascending order, starting from the value of the factor.


____________________________________________________________________________________________
Example_01

Input
2
5

Output
[2, 4, 6, 8, 10]


____________________________________________________________________________________________
Example_02

Input
1
10

Output
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

"""