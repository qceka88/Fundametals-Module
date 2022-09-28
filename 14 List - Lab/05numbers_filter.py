lines = int(input())

initial_list = []

for number in range(lines):
    current_number = int(input())
    initial_list.append(current_number)

command = input()

filtered_number = []
for filter_number in initial_list:
    if command == 'even':
        if filter_number % 2 == 0:
            filtered_number.append(filter_number)
    elif command == 'odd':
        if filter_number % 2 != 0:
            filtered_number.append(filter_number)
    elif command == 'positive':
        if filter_number >= 0:
            filtered_number.append(filter_number)
    elif command == 'negative':
        if filter_number < 0:
            filtered_number.append(filter_number)

print(filtered_number)





#################################### TASK CONDITION ############################
"""
                               5.	Numbers Filter
On the first line, you will receive a single number n. 
On the following n lines, you will receive integers. 
After that, you will be given one of the following commands:
•	even
•	odd
•	negative
•	positive
Filter all the numbers that fit in the category (0 counts as a positive and even). 
Finally, print the result.


____________________________________________________________________________________________
Example_01

Input
5
33
19
-2
18
998
even

Output
[-2, 18, 998]


____________________________________________________________________________________________
Example_02

Input
3
111
-4
0
negative

Output
[-4]

"""