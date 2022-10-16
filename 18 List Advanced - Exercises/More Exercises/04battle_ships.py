def attack(battle_field, x_row, y_col):
    destroy = False
    if battle_field[x_row][y_col] > 0:
        battle_field[x_row][y_col] -= 1
        if battle_field[x_row][y_col] == 0:
            destroy = True
    return battle_field, destroy


rows = int(input())
game_field = []

for row in range(rows):
    new_row = list(map(int, input().split()))
    game_field.append(new_row)

moves = input().split()

destroyed_ships = 0

for move in moves:
    movement = move.split('-')
    row = int(movement[0])
    col = int(movement[1])
    game_field, ship_destroyed = attack(game_field, row, col)
    if ship_destroyed:
        destroyed_ships += 1

print(destroyed_ships)



#################################### TASK CONDITION ############################
"""
4.	Battle Ships
You will be given a number n representing the number of rows of the field. 
On the following n lines, you will receive each field row as a string 
with numbers separated by a space. Each number greater than zero 
represents a ship with health equal to the number value. 
After that, you will receive the squares that are being 
attacked in the format: "{row}-{col} {row}-{col}". Each time a square 
is being attacked, if there is a ship (number greater than 0), you should 
reduce its value by 1. If a ship's health reaches zero, it is destroyed. 
After the attacks have ended, print how many ships were destroyed.


____________________________________________________________________________________________
Example_01

Input
3
1 0 0 1
2 0 0 0
0 3 0 1
0-0 1-0 2-1 2-1 2-1 1-1 2-1	

Output
2

Explanation
States after each attack:
First attack -> 1 ship destroyed
0 0 0 1
2 0 0 0
0 3 0 1
Second attack -> reduce ship health
0 0 0 1
1 0 0 0
0 2 0 1
Third attack -> reduce ship health
0 0 0 1
2 0 0 0
0 2 0 1
Fourth attack -> reduce ship health 
0 0 0 1
2 0 0 0
0 1 0 1
Fifth attack -> another ship destroyed
0 0 0 1
2 0 0 0
0 0 0 1
Sixth and Seventh attack -> no ship destroyed


____________________________________________________________________________________________
Example_02

Input
5
1 0 5 0 1
6 3 9 0 0
7 9 4 3 2
1 0 0 4 9
5 6 0 3 5
0-1 0-2 0-2 0-2 0-2 0-2 3-0

Output
2

"""
