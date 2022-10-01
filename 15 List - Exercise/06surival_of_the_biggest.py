list_of_integers = list(map(int, input().split()))
count = int(input())

for remove in range(count):
    min_number = min(list_of_integers)
    list_of_integers.remove(min_number)

print(*list_of_integers, sep=", ")


#################################### TASK CONDITION ############################
"""
                    6.	Survival of the Biggest
Write a program that receives a list of integer numbers (separated by a single space) and a number n. 
The number n represents the count of numbers to remove from the list.
You should remove the smallest ones, and then, you should print all the numbers
that are left in the list, separated by a comma and a space ", ".


____________________________________________________________________________________________
Example_01

Input
10 9 8 7 6 5
3

Output
10, 9, 8


____________________________________________________________________________________________
Example_02

Input
1 10 2 9 3 8
2

Output
10, 9, 3, 8

"""
