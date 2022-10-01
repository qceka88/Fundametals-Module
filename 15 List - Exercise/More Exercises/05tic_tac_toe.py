def game(matrix, player):
    # row check
    if matrix[0][0] == matrix[0][1] == matrix[0][2] == player \
            or matrix[1][0] == matrix[1][1] == matrix[1][2] == player \
            or matrix[2][0] == matrix[2][1] == matrix[2][2] == player:
        return True
    # col check
    elif matrix[0][0] == matrix[1][0] == matrix[2][0] == player \
            or matrix[0][1] == matrix[1][1] == matrix[2][1] == player \
            or matrix[0][2] == matrix[1][2] == matrix[2][2] == player:
        return True
    # diagonals check
    elif matrix[0][0] == matrix[1][1] == matrix[2][2] == player \
            or matrix[2][0] == matrix[1][1] == matrix[0][2] == player:
        return True
    else:
        return False


game_field = []

first_player = '1'
second_player = '2'

for row in range(3):
    current_row = input().split()
    game_field.append(row)

player01 = game(game_field, first_player)
player02 = game(game_field, second_player)

if player01 and player02 == False:
    print('First player won')
elif player02 and player01 == False:
    print('Second player won')
else:
    print('Draw!')

#################################### TASK CONDITION ############################
"""
5.	Tic-Tac-Toe
You will receive a field of a tic-tac-toe game in three lines containing numbers, 
separated by a single space.
Legend:
•	0 - empty space
•	1 - first player move
•	2 - second player move
Find out who the winner is. If the first player wins, print "First player won".
 If the second player wins, print "Second player won". Otherwise, print "Draw!".


____________________________________________________________________________________________
Example_01

Input
2 0 1
0 1 0
1 0 2

Output
First player won


____________________________________________________________________________________________
Example_02

Input
0 1 0
2 1 2
1 1 0

Output
Second player won


____________________________________________________________________________________________
Example_01

Input
1 0 2
0 1 2
1 2 2

Output
Draw!

"""
