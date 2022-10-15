#################### variant 01 #######################
number_of_rooms = int(input())

free_chairs = 0
enough_chairs = True

for room in range(1, number_of_rooms + 1):
    input_data = input().split()
    current_chairs = len(input_data[0])
    visitors = int(input_data[1])
    diff = abs(visitors - current_chairs)
    if visitors > current_chairs:
        print(f'{diff} more chairs needed in room {room}')
        enough_chairs = False
    else:
        free_chairs += diff

if enough_chairs:
    print(f"Game On, {free_chairs} free chairs left")

#################### variant 02 #######################

def check_room(input_data):
    current_chairs = len(input_data[0])
    visitors = int(input_data[1])
    diff = current_chairs - visitors
    return diff


number_of_rooms = int(input())

free_chairs = 0
enough_chairs = True

for room in range(1, number_of_rooms + 1):
    input_line = input().split()
    checking = check_room(input_line)
    if checking >= 0:
        free_chairs += checking
    else:
        print(f'{abs(checking)} more chairs needed in room {room}')
        enough_chairs = False

if enough_chairs:
    print(f"Game On, {free_chairs} free chairs left")



#################################### TASK CONDITION ############################
"""
                         5.	Office Chairs
You are a facility manager at a large business center. 
One of your responsibilities is to check if each conference room 
in the center has enough chairs for the visitors.
On the first line, you will be given an integer n representing the 
number of rooms in the business center. On the following n lines for each room, 
you will receive information about the chairs in the room and the 
number of visitors. Each chair will be presented with the char "X". 
Next, there will be a single space and the number of visitors at the end. 
For example: "XXXXX 4" (5 chairs and 4 visitors). 
Keep track of the free chairs:
•	If there are not enough chairs in a specific room, 
print the following message: "{needed_chairs_in_room} more chairs 
needed in room {number_of_room}". The rooms start from 1.
•	Otherwise, print: "Game On, {total_free_chairs} free chairs left".


____________________________________________________________________________________________
Example_01

Input
4
XXXX 4
XX 1
XXXXXX 3
XXX 3

Output
Game On, 4 free chairs left


____________________________________________________________________________________________
Example_02

Input
3
XXXXXXX 5
XXXX 5
XXXXXX 8

Output
1 more chairs needed in room 2
2 more chairs needed in room 3

"""
