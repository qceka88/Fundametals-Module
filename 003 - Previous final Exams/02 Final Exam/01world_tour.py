travel = input()

while True:
    command = input()
    if command == 'Travel':
        break
    input_data = command.split(':')
    action = input_data[0]
    if action == 'Add Stop':
        index = int(input_data[1])
        new_stop = input_data[2]
        if len(travel) > index >= 0:
            travel = travel[:index] + new_stop + travel[index:]
    elif action == 'Remove Stop':
        start = int(input_data[1])
        end = int(input_data[2])
        if len(travel) > start >= 0 and len(travel) > end >= 0:
            travel = travel[:start] + travel[end + 1:]
    elif action == 'Switch':
        old_stop = input_data[1]
        new_stop = input_data[2]
        travel = travel.replace(old_stop, new_stop)
    print(travel)
print(f"Ready for world tour! Planned stops: {travel}")

#################################### TASK CONDITION ############################
"""
                              Problem 1 - World Tour
Problem for exam preparation for the Programming Fundamentals Course @SoftUni.
Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2518#0.

You are a world traveler, and your next goal is to make a world tour.
To do that, you have to plan out everything first.
To start with, you would like to plan out all of your stops where you will have a break.
On the first line, you will be given a string containing all of your stops.
Until you receive the command "Travel",
you will be given some commands to manipulate that initial string. The commands can be:
•	"Add Stop:{index}:{string}":
o	Insert the given string at that index only if the index is valid
•	"Remove Stop:{start_index}:{end_index}":
o	Remove the elements of the string from the starting index to the end index (inclusive) if both indices are valid
•	"Switch:{old_string}:{new_string}":
o	If the old string is in the initial string, replace it with the new one (all occurrences)
Note: After each command, print the current state of the string if it is valid!
After the "Travel" command, print the following: "Ready for world tour! Planned stops: {string}"
Input / Constraints
•	JavaScript: you will receive a list of strings
•	An index is valid if it is between the first and the last element index (inclusive) (0 ….. Nth) in the sequence.
Output
•	Print the proper output messages in the proper cases as described in the problem description

____________________________________________________________________________________________
Example

Input
Hawai::Cyprys-Greece
Add Stop:7:Rome
Remove Stop:11:16
Switch:Greece:Bulgaria
Travel

Output
Hawai::RomeCyprys-Greece
Hawai::Rome-Greece
Bulgaria::Rome-Greece
Ready for world tour! Planned stops: Bulgaria::Rome-Greece

"""