fire_cells = input().split('#')
water_level = int(input())

cells_list = []

for cell in fire_cells:
    command = cell.split(' = ')
    type_of_fire = command[0]
    value_of_cell = int(command[1])
    if type_of_fire == 'High':
        if 81 <= value_of_cell <= 125:
            if water_level - value_of_cell >= 0:
                water_level -= value_of_cell
                cells_list.append(value_of_cell)
    elif type_of_fire == 'Medium':
        if 51 <= value_of_cell <= 80:
            if water_level - value_of_cell >= 0:
                water_level -= value_of_cell
                cells_list.append(value_of_cell)
    elif type_of_fire == 'Low':
        if 1 <= value_of_cell <= 50:
            if water_level - value_of_cell >= 0:
                water_level -= value_of_cell
                cells_list.append(value_of_cell)

total_effort = sum(cells_list) * 0.25

print('Cells:')
for fire in cells_list:
    print(f' - {fire}')
print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {sum(cells_list)}")


#################################### TASK CONDITION ############################
"""
                    8.	* Seize the Fire
The group of adventurists has gone on their first task. Now they should walk through fire - literally. 
They should use all the water they have left. Your task is to help them survive.
Create a program that calculates the water needed to put out a "fire cell", 
based on the given information about its "fire level" and how much it gets affected by water.
First, you will be given the level of fire inside the cell with the integer value of the cell, 
which represents the needed water to put out the fire.  They will be given in the following format:
"{typeOfFire} = {valueOfCell}#{typeOfFire} = {valueOfCell}# … {typeOfFire} = {valueOfCell}"
Afterward you will receive the amount of water you have for putting out the fires.
There is a range of fire for each fire type, and if a cell's value is below or exceeds it,
it is invalid, and you do not need to put it out.
Type of Fire	Range
High	81 - 125
Medium	51 - 80
Low	1 - 50
If a cell is valid, you should put it out by reducing the water with its value.
Putting out fire also takes effort, and you need to calculate it. 
Its value is equal to 25% of the cell's value. In the end, you will have to print the total effort.
Keep putting out cells until you run out of water. Skip it and try the next one
if you do not have enough water to put out a given cell. In the end, print the cells
you have put out in the following format:
"Cells:
 - {cell1}
 - {cell2}
 …
 - {cellN}"
"Effort: {effort}"
The effort should be formatted to the second decimal place. 
In the end, print the total fire you have put out from all the cells in the following format: 
"Total Fire: {total_fire}"
Input / Constraints
•	On the 1st line, you will receive the fires with their cells
 in the format described above – integer numbers in the range [1…500].
•	On the 2nd line, you will receive the water – an integer number in the range [0….100000].
Output
Print the output as described above.


____________________________________________________________________________________________
Example_01

Input
High = 89#Low = 28#Medium = 77#Low = 23
1250

Output
Cells:
 - 89
 - 28
 - 77
 - 23
Effort: 54.25
Total Fire: 217

Explanation
After reading the output, we start checking the level of the fire and its validity. 
The first is valid, so we subtract the 89 from the amount of water – 1250, and the water becomes 1161. 
We need to calculate the effort, which is 25% of 89. We will add 89 to the total fire we have put out. I
n the end, the effort is 54.22 and the total fire: 217


____________________________________________________________________________________________
Example_02

Input
High = 150#Low = 55#Medium = 86#Low = 40#High = 110#Medium = 77
220

Output
Cells:
 - 40
 - 110
Effort: 37.50
Total Fire: 150

"""
