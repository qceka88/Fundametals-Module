unsorted_names = input().split(', ')
sorting = lambda x: (-len(x), x)
print(sorted(unsorted_names, key=sorting))


#################################### TASK CONDITION ############################
"""
             5.	Sorting Names
Write a program that reads a single string with 
names separated by comma and space ", ". 
Sort the names by their length in descending order. 
If 2 or more names have the same length, sort them in 
ascending order (alphabetically). Print the resulting list.


____________________________________________________________________________________________
Example_01

Input
Ali, Marry, Kim, Teddy, Monika, John

Output
["Monika", "Marry", "Teddy", "John", "Ali", "Kim"]


____________________________________________________________________________________________
Example_02

Input
Lilly, Tim, Kate, Tom, Alex

Output
['Lilly', 'Alex', 'Kate', 'Tim', 'Tom']

"""
