def calculation(first_side, second_side):
    calculated_area = first_side * second_side
    return calculated_area


side_a = int(input())
side_b = int(input())

area = calculation(side_a, side_b)

print(area)

#################################### TASK CONDITION ############################
"""
                       6.	Calculate Rectangle Area
                       
Create a function that calculates and returns the area of a rectangle
by given width and height. Print the result on the console.


____________________________________________________________________________________________
Example_01

Input
3
4

Output
12


____________________________________________________________________________________________
Example_02

Input
6
2

Output
12

"""
