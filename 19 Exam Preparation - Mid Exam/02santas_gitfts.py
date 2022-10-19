moves_number = int(input())
houses_str = input().split()
houses = [int(house) for house in houses_str if 1 <= int(house) <= 500]
current_position = 0
for move in range(moves_number):
    input_data = input().split()
    command = input_data[0]
    index = int(input_data[1])

    if command == 'Forward':
        if (index + current_position) in range(len(houses)):
            current_position += index
            houses.pop(current_position)
    elif command == 'Back':
        if (current_position - index) in range(len(houses)):
            current_position -= index
            houses.pop(current_position)
    elif command == 'Gift' and index in range(len(houses)):
        current_position = index
        house = int(input_data[2])
        if 1 <= house <= 500:
            houses.insert(index, house)
    elif command == 'Swap':
        first_house_value = index
        second_house_value = int(input_data[2])
        if first_house_value in houses and second_house_value in houses:
            first_index = houses.index(first_house_value)
            second_index = houses.index(second_house_value)
            houses[first_index], houses[second_index] = houses[second_index], houses[first_index]

print(f'Position: {current_position}')
print(*houses, sep=', ')



#################################### TASK CONDITION ############################
"""
                              Santa’s Gifts
You will be given an array of integers, which represent the house numbers you should visit. 
The commands will lead you to them. If they lead you to non-existing places, don’t move.
•	Forward {numberOfSteps}
•	Back {numberOfSteps}
o	When you receive the “Forward” or “Back” command, you move the given number 
of times in this direction and remove the house in this position from your list. 
Also, when you receive the next command, you continue from this position. 
•	Gift {index} {houseNumber}
o	Enter a new house number, which the dwarves have left out on purpose, 
at the given position and move to its position. 
•	Swap {indexOfFirst} {indexOfSecond}
o	Santa wants to rearrange his path and swap the order of two houses. 
You will receive the numbers of the houses, that need to be switched 
and he doesn’t need to move to fulfill this command.
Input 
•	On the first line you will receive the number of commands – integer in the range [1-50]
•	On the second line you will receive the array of integers, 
that represent the houses, split by a single space – valid integers in the range [1 – 500]
•	On the next n lines, you will receive the commands in the following format:
o	Forward {steps}
o	Back {steps}
o	Gift {index} {value}
o	Swap {value1} {value2}
Output
•	Print the last position and the remaining houses in the following format:
“Position {position}”
“{houseNumber}, {houseNumber}………, {houseNumber}”
Constraints
•	The house numbers will be valid integers in the range [1 - 1000]
•	The number of commands will be a valid integer in the range [1 - 50]
•	The commands will be given in the exact format as they are written above
•	There will always be at least one valid command


____________________________________________________________________________________________
Example_01

Input
255 500 54 78 98 24 30 47 69 58
Forward 1
Swap 54 47
Gift 1 20
Back 1
Forward 3

Output
Position: 3
20, 47, 78, 24, 30, 54, 69, 58	First, we receive the “Forward” command, 
the sleigh will start from the beginning – index 0. He has to move 1 step,
 so he will move to index 1 and delete the house number, which is stored there – 500. What is left of the list:
255 54 78 98 24 30 47 69 58
and Santa’s position is 1.
The next command is “Swap”. After it, the list looks like this:
255 47 78 98 24 30 54 69 58 and Santa’s position doesn’t change.
The “Gift” command has to insert at index 1 the house with number 20:
255 20 47 78 98 24 30 54 69 58 and move Santa to current index – 1.
The “Back” command has to move Santa back 1 step from his current position. 
He is at 1 position, so he has to move back to position 0, and remove the house number, which it stores:
20 47 78 98 24 30 54 69 58
The last “Forward” command will move him three steps forward from his current 
position, which is 0, so he goes to – 3 and removes the house:
20 47 78 24 30 54 69 58
6
50 40 25 63 78 54 66 77 24 87
Forward 4
Back 3
Forward 3
Gift 2 88
Swap 50 87
Forward 1	Position: 3
87, 25, 88, 54, 77, 24, 50	

"""
