############################### variant 01 #########################
sequence_of_numbers = list(map(int, input().split(', ')))

group = 10

while len(sequence_of_numbers) > 0:
    current_group = [num for num in sequence_of_numbers if num <= group]
    for number in current_group:
        if number in sequence_of_numbers:
            sequence_of_numbers.remove(number)
    print(f"Group of {group}'s: {current_group}")
    group += 10

############################### variant 01 #########################

sequence_of_numbers = list(map(int, input().split(', ')))
group = 10

while len(sequence_of_numbers) > 0:
    current_group = [num for num in sequence_of_numbers if num <= group]
    removing = [sequence_of_numbers.remove(number) for number in current_group if number in sequence_of_numbers]
    print(f"Group of {group}'s: {current_group}")
    group += 10


#################################### TASK CONDITION ############################
"""
7.	Group of 10's
Write a program that receives a sequence of numbers 
(a string containing integers separated by ", ") and prints the numbers 
sorted into lists of 10's in the format "Group of {group}'s: {list_of_numbers}".
Examples:
•	The numbers 2, 8, 4, and 10 fall into the group of 10's.
•	The numbers 13, 19, 14, and 15 fall into the group of 20's.
For more clarification, see the examples below.


____________________________________________________________________________________________
Example_01

Input
8, 12, 38, 3, 17, 19, 25, 35, 50

Output
Group of 10's: [8, 3]
Group of 20's: [12, 17, 19]
Group of 30's: [25]
Group of 40's: [38, 35]
Group of 50's: [50]


____________________________________________________________________________________________
Example_02

Input
1, 3, 3, 4, 34, 35, 25, 21, 33

Output
Group of 10's: [1, 3, 3, 4]
Group of 20's: []
Group of 30's: [25, 21]
Group of 40's: [34, 35, 33]

"""
