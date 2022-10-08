from math import sqrt, floor


def line_calculation(first01, second01, first02, second02):
    calculated_distance = (abs(first01) ** 2) + (abs(second01) ** 2) + (abs(first02) ** 2) + (abs(second02) ** 2)
    return sqrt(calculated_distance)


def closest_point(first01, second01, first02, second02):
    result = []
    line01 = abs(first01) ** 2 + abs(second01) ** 2
    line02 = abs(first02) ** 2 + abs(second02) ** 2
    if line01 <= line02:
        result = [(floor(first01), floor(second01)), (floor(first02), floor(second02))]
    else:
        result = [(floor(first02), floor(second02)), (floor(first01), floor(second01))]
    return result


line = 0
points = []

for point in range(2):
    x1 = float(input())
    y1 = float(input())
    x2 = float(input())
    y2 = float(input())
    line_check = line_calculation(x1, y1, x2, y2)
    if line < line_check:
        line = line_check
        points = closest_point(x1, y1, x2, y2)

print(*points, sep='')




#################################### TASK CONDITION ############################
"""
                          3.	Longer Line
You will be given the coordinates of four points. 
The first and the second pair of points form two different lines. 
Create a function that prints the longer line in the format "({X1}, {Y1})({X2}, {Y2})" 
starting from the point which is closer to the center of the coordinate system (0, 0). 
You can reuse the method that you wrote for the previous problem. 
If the lines are of equal length, print only the first one. 
The resulting coordinates must be formatted to the lower integer.


____________________________________________________________________________________________
Example_01

Input
2
4
-1
2
-5
-5
4
-3

Output
(4, -3)(-5, -5)


____________________________________________________________________________________________
Example_02

Input
1
2
3
4
9
7
5
6

Output
(5, 6)(9, 7)

"""
