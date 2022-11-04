from collections import defaultdict

input_line = input().replace(' ', '')

data = defaultdict(int)

for character in input_line:
    data[character] += 1

for char, occurrences in data.items():
    print(f"{char} -> {occurrences}")




#################################### TASK CONDITION ############################
"""
                        1.	Count Chars in a String
Write a program that counts all characters in a string except for space (" "). 
Print all the occurrences in the following format:
"{char} -> {occurrences}"


____________________________________________________________________________________________
Example_01

Input
text

Output
t -> 2
e -> 1
x -> 1


____________________________________________________________________________________________
Example_01

Input
text text text

Output
t -> 6
e -> 3
x -> 3

"""
