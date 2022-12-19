pirate_ship = list(map(int, input().split('>')))
war_ship = list(map(int, input().split('>')))
max_health = int(input())

finished_battle = False
destroyed = False

while destroyed is not True:
    input_line = input()
    if input_line == 'Retire':
        finished_battle = True
        break
    input_data = input_line.split()
    command = input_data[0]
    if command == 'Fire':
        index = int(input_data[1])  # warship index
        if index >= 0 and index < len(war_ship):
            damage = int(input_data[2])
            if war_ship[index] - damage <= 0:
                print("You won! The enemy ship has sunken.")
                break
            war_ship[index] -= damage
    elif command == 'Defend':
        start_index = int(input_data[1])  # start_index of pirate ship
        end_index = int(input_data[2])  # end_index of pirate ship
        if start_index >= 0 and start_index < len(pirate_ship):
            if end_index >= 0 and end_index < len(pirate_ship):
                damage = int(input_data[3])
                for ship_block in range(start_index, end_index + 1):
                    if pirate_ship[ship_block] - damage <= 0:
                        print(f"You lost! The pirate ship has sunken.")
                        destroyed=True
                        break
                    pirate_ship[ship_block] -= damage
    elif command == 'Repair':
        block_index = int(input_data[1])  # index of Pirate ship block for repair
        if block_index >= 0 and block_index < len(pirate_ship):
            health = int(input_data[2])
            if pirate_ship[block_index] + health > max_health:
                pirate_ship[block_index] = max_health
            else:
                pirate_ship[block_index] += health
    elif command == 'Status':
        block_for_repair = 0
        for block in pirate_ship:
            if block < (max_health * 0.2):
                block_for_repair += 1
        print(f"{block_for_repair} sections need repair.")

if finished_battle:
    print(f"Pirate ship status: {sum(pirate_ship)}")
    print(f'Warship status: {sum(war_ship)}')



#################################### TASK CONDITION ############################
"""
                      Problem 3 - Man-O-War
Problem for exam preparation for the Programming Fundamentals Course @SoftUni.
Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/1773#2.

The pirates encounter a huge Man-O-War at sea. 
Create a program that tracks the battle and either chooses a winner or prints a stalemate.
 On the first line, you will receive the status of the pirate ship, 
 which is a string representing integer sections separated by ">".
  On the second line, you will receive the same type of status, but for the warship: 
"{section1}>{section2}>{section3}… {sectionn}"
On the third line, you will receive the maximum health capacity a section of the ship can reach. 
The following lines represent commands until "Retire":
•	"Fire {index} {damage}" - the pirate ship attacks the warship with the given damage at that section.
 Check if the index is valid and if not, skip the command. If the section breaks (health <= 0) the warship sinks,
  print the following and stop the program: "You won! The enemy ship has sunken."
•	"Defend {startIndex} {endIndex} {damage}" - the warship attacks the pirate ship 
with the given damage at that range (indexes are inclusive). Check if both indexes are valid and if not,
 skip the command. If the section breaks (health <= 0) the pirate ship sinks, print the following and stop the program:
"You lost! The pirate ship has sunken."
•	"Repair {index} {health}" - the crew repairs a section of the pirate ship with the given health. 
Check if the index is valid and if not, skip the command. 
The health of the section cannot exceed the maximum health capacity.
•	"Status" - prints the count of all sections of the pirate ship that need repair soon, 
which are all sections that are lower than 20% of the maximum health capacity. Print the following:
"{count} sections need repair."
In the end, if a stalemate occurs, print the status of both ships, which is the sum of their individual sections, 
in the following format:
"Pirate ship status: {pirateShipSum}
Warship status: {warshipSum}"
Input
•	On the 1st line, you are going to receive the status of the pirate ship (integers separated by '>')
•	On the 2nd line, you are going to receive the status of the warship
•	On the 3rd line, you will receive the maximum health a section of a ship can reach.
•	On the following lines, until "Retire", you will be receiving commands.
Output
•	Print the output in the format described above.
Constraints
•	The section numbers will be integers in the range [1….1000]
•	The indexes will be integers [-200….200]
•	The damage will be an integer in the range [1….1000]
•	The health will be an integer in the range [1….1000]


____________________________________________________________________________________________
Example_01


Input
12>13>11>20>66
12>22>33>44>55>32>18
70
Fire 2 11
Fire 8 100
Defend 3 6 11
Defend 0 3 5
Repair 1 33
Status
Retire

Output
2 sections need repair.
Pirate ship status: 135
Warship status: 205

Explanation
First, we receive the command "Fire 2 11", and damage the warship at section index 2,
 which is currently 33, and after reduction, the status of the warship is the following:
12 22 22 44 55 32 18
The second and third commands have invalid indexes, so we skip them.
The fourth command, "Defend 0 3 5" damages 4 sections of the pirate ship with 5, which results in the following states:
7 8 6 15 66
The fifth command, "Repair 1 33" repairs the pirate ship section and adds 33 health to the current 8, 
which results in 41
Only 2 sections of the pirate ship (7 and 6) need repair soon.
In the end, there is a stalemate, so we print both ship statuses (sum of all sections).


____________________________________________________________________________________________
Example_02


Input
2>3>4>5>2
6>7>8>9>10>11
20
Status
Fire 2 3
Defend 0 4 11
Repair 3 18
Retire

Output
3 sections need repair.
You lost! The pirate ship has sunken.

"""