def absolute(input_data):
    output_list = []
    for number in input_data:
        converted_number = float(number)
        output_list.append(abs(converted_number))
    return output_list


input_line = input().split()
absolute_values = absolute(input_line)

print(absolute_values)



#################################### TASK CONDITION ############################
"""
                       1.	Absolute Values
Write a program that receives a sequence of numbers,
separated by a single space, 
and prints their absolute value as a list. Use abs().


____________________________________________________________________________________________
Example_01

Input
1 2.5 -3 -4.5

Output
[1.0, 2.5, 3.0, 4.5]


____________________________________________________________________________________________
Example_02

Input
-0 1 10 -6.66
[0.0, 1.0, 10.0, 6.66]

"""
