def int_data(input_data):
    integer = int(input_data) * 2
    return integer


def real_data(input_data):
    real = float(input_data) * 1.5
    return f'{real:.2f}'


def string_data(input_data):
    return f'${input_data}$'


data_type = input()
data = input()

if data_type == 'int':
    result = int_data(data)
elif data_type == 'real':
    result = real_data(data)
elif data_type == 'string':
    result = string_data(data)

print(result)




#################################### TASK CONDITION ############################
"""
1.	Data Types
Write a function that, depending on the first line of the input,
reads one of the following strings: "int", "real", or "string".
•	If the data type is an int, multiply the number by 2.
•	If the data type is real, multiply the number by 1.5 and
format the result to the second decimal point.
•	If the data type is a string, surround the input with "$".
Print the result on the console.


____________________________________________________________________________________________
Example_01

Input
int
5

Output
10


____________________________________________________________________________________________
Example_02

Input
real
2

Output
3.00


____________________________________________________________________________________________
Example_03

Input
string
hello

Output
$hello$
____________________________________________________________________________________________



Hint
Try to solve the problem using only one method with different overloads.

"""
