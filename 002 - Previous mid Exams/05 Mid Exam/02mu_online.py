dungeon = input().split('|')

health = 100
bitcoin = 0
room = 0

dead = False
for command in dungeon:
    room += 1
    order, amount = command.split(' ')
    if order == 'potion':
        if health + int(amount) > 100:
            diff = 100 - health
            print(f"You healed for {diff} hp.")
            health = 100
        else:
            health += int(amount)
            print(f"You healed for {amount} hp.")
        print(f"Current health: {health} hp.")
    elif order == 'chest':
        bitcoin += int(amount)
        print(f"You found {amount} bitcoins.")
    else:
        if health - int(amount) <= 0:
            print(f"You died! Killed by {order}.")
            print(f"Best room: {room}")
            dead = True
            break
        else:
            health -= int(amount)
            print(f"You slayed {order}.")
if dead is not True:
    print(f"You've made it!\nBitcoins: {bitcoin}\nHealth: {health}")

#################################### TASK CONDITION ############################
"""
                   Problem 2. Mu Online
Problem for exam preparation for the Programming Fundamentals Course @SoftUni.
Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2028#1.

You have initial health 100 and initial bitcoins 0. You will be given a string
 representing the dungeon's rooms. Each room is separated with '|' (vertical bar): "room1|room2|room3…"
Each room contains a command and a number, separated by space. The command can be:
•	"potion"
o	You are healed with the number in the second part. But your health cannot exceed your initial health (100).
o	First print: "You healed for {amount} hp."
o	After that, print your current health: "Current health: {health} hp."
•	"chest"
o	You've found some bitcoins, the number in the second part.
o	Print: "You found {amount} bitcoins."
•	In any other case, you are facing a monster, which you will fight. 
The second part of the room contains the attack of the monster. You should remove the monster's attack from your health. 
o	If you are not dead (health <= 0), you've slain the monster, and you should print: "You slayed {monster}."
o	If you've died, print "You died! Killed by {monster}." and your quest is over. 
Print the best room you've manage to reach: "Best room: {room}"
If you managed to go through all the rooms in the dungeon, print on the following three lines: 
"You've made it!"
"Bitcoins: {bitcoins}"
"Health: {health}"
Input / Constraints
You receive a string representing the dungeon's rooms, separated with '|' (vertical bar): "room1|room2|room3…".
Output
Print the corresponding messages described above.

____________________________________________________________________________________________
Example_01

Input
rat 10|bat 20|potion 10|rat 10|chest 100|boss 70|chest 1000	You slayed rat.

Output
You slayed bat.
You healed for 10 hp.
Current health: 80 hp.
You slayed rat.
You found 100 bitcoins.
You died! Killed by boss.
Best room: 6

____________________________________________________________________________________________
Example_02

Input
cat 10|potion 30|orc 10|chest 10|snake 25|chest 110	You slayed cat.

Output
You healed for 10 hp.
Current health: 100 hp.
You slayed orc.
You found 10 bitcoins.
You slayed snake.
You found 110 bitcoins.
You've made it!
Bitcoins: 120
Health: 65


"""