##################################### variant 01 #####################################

class MovesCounter:

    def __init__(self, some_maze):
        self.some_maze = some_maze

    def counter(self):
        number = 0
        for row in range(len(self.some_maze)):
            for col in range(len((self.some_maze[row]))):
                if self.some_maze[row][col] == 'k' or self.some_maze[row][col] == ' ':
                    number += 1
        return number

    #          >>>>>>    Comprehension Variant Of Moves Counter.counter()   <<<<<
    # def counter(self):
    #     moves = len(
    #         [self.some_maze[row][col] for row in range(len(self.some_maze)) for col in range(len(self.some_maze[row]))
    #          if self.some_maze[row][col] == 'k' or self.some_maze[row][col] == ' '])
    #     return moves


class LocateKate:

    def __init__(self, labyrinth):
        self.labyrinth = labyrinth

    def find_that_girl(self):
        kate_row = 0
        kate_col = 0
        for row_index in range(len(self.labyrinth)):
            for col_index in range(len(self.labyrinth[row_index])):
                if self.labyrinth[row_index][col_index] == 'k':
                    kate_row = row_index
                    kate_col = col_index
        return kate_row, kate_col


class Boundary:

    def __init__(self, maze):
        self.maze = maze

    def is_on_exit(self):
        for row in range(len(self.maze)):
            for col in range(len(self.maze[row])):
                if row == 0 or row == len(self.maze) - 1 or col == 0 or col == len(self.maze[row]) - 1:
                    if self.maze[row][col] == 'k':
                        return True
        return False


class Moving:

    def __init__(self, maze, kate_row, kate_col):
        self.maze = maze
        self.kate_row = kate_row
        self.kate_col = kate_col

    def move_kate(self):
        while True:
            is_on_boundary = Boundary(self.maze).is_on_exit()
            if is_on_boundary:
                return self.maze
            elif self.maze[self.kate_row][self.kate_col + 1] == ' ':
                self.maze[self.kate_row][self.kate_col + 1] = 'k'
                self.kate_col += 1
            elif self.maze[self.kate_row][self.kate_col - 1] == ' ':
                self.maze[self.kate_row][self.kate_col - 1] = 'k'
                self.kate_col -= 1
            elif self.maze[self.kate_row + 1][self.kate_col] == ' ':
                self.maze[self.kate_row + 1][self.kate_col] = 'k'
                self.kate_row += 1
            elif self.maze[self.kate_row - 1][self.kate_col] == ' ':
                self.maze[self.kate_row - 1][self.kate_col] = 'k'
                self.kate_row -= 1
            elif self.maze[self.kate_row][self.kate_col + 1] != ' ' \
                    and self.maze[self.kate_row][self.kate_col - 1] != ' ' \
                    and self.maze[self.kate_row + 1][self.kate_col] != ' ' \
                    and self.maze[self.kate_row - 1][self.kate_col] != ' ':
                return False


class FindKate:

    def __init__(self, some_maze):
        self.some_maze = some_maze

    def location(self):
        location_object = LocateKate(self.some_maze)
        return location_object.find_that_girl()

    def result(self):
        row, col = self.location()
        is_found = Moving(self.some_maze, row, col).move_kate()
        if is_found != False:
            maze_with_moves = is_found
            moves = MovesCounter(maze_with_moves).counter()
            return moves
        return False

    def __repr__(self):
        if self.result():
            return f'Kate got out in {self.result()} moves'
        return 'Kate cannot get out'


rows_number = int(input())
game_field = []

for row in range(rows_number):
    current_row = input()
    game_field.append(list(current_row))

output = FindKate(game_field)
print(output)

##################################### variant 02 #####################################

rows_number = int(input())
maze = []

for row in range(rows_number):
    current_row = input()
    maze.append(list(current_row))

kate_row = 0
kate_col = 0

# [c] is for column index. [r] for row index
for r in range(len(maze)):
    for c in range(len(maze[r])):
        if maze[r][c] == 'k':
            kate_row = r
            kate_col = c

kate_grate_escape = False

while True:

    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if row == 0 or row == len(maze) - 1 or col == 0 or col == len(maze[row]) - 1:
                if maze[row][col] == 'k':
                    kate_grate_escape = True
                    break

    if kate_grate_escape:
        break
    elif maze[kate_row][kate_col + 1] == ' ':
        maze[kate_row][kate_col + 1] = 'k'
        kate_col += 1
    elif maze[kate_row][kate_col - 1] == ' ':
        maze[kate_row][kate_col - 1] = 'k'
        kate_col -= 1
    elif maze[kate_row + 1][kate_col] == ' ':
        maze[kate_row + 1][kate_col] = 'k'
        kate_row += 1
    elif maze[kate_row - 1][kate_col] == ' ':
        maze[kate_row - 1][kate_col] = 'k'
        kate_row -= 1
    elif maze[kate_row][kate_col + 1] != ' ' \
            and maze[kate_row][kate_col - 1] != ' ' \
            and maze[kate_row + 1][kate_col] != ' ' \
            and maze[kate_row - 1][kate_col] != ' ':
        break

if kate_grate_escape:
    moves = len([maze[row][col] for row in range(len(maze)) for col in range(len(maze[row])) if
                 maze[row][col] == 'k' or maze[row][col] == ' '])
    print(f'Kate got out in {moves} moves')
else:
    print('Kate cannot get out')

#################################### TASK CONDITION ############################
"""
                        3.	Kate's Way Out
Kate is stuck in a maze. You should help her to find her way out.
On the first line, you will be given how many rows there are in the maze. 
On the following n lines, you will be given the maze itself. Here is a legend for the maze:
•	"#" - means a wall; Kate cannot go through there
•	" " - means empty space; Kate can go through there
•	"k" - the initial position of Kate; start looking for a way out from there
There are two options: Kate either gets out or not:
•	If Kate can get out, print the following: 
"Kate got out in {number_of_moves} moves". 
Note: If there are two or more ways out, she always chooses the longest one.
•	Otherwise, print: "Kate cannot get out".


____________________________________________________________________________________________
Example_01

Input
4
######
##  k#
## ###
## ###

Output
Kate got out in 5 moves

____________________________________________________________________________________________
Example_02

Input
5
######
##  k#
## ###
######
## ###

Output
Kate cannot get out

"""
