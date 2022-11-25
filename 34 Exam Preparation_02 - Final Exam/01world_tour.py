##################################### variant 01 #####################################

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


##################################### variant 02 #####################################
class AddStop:

    def __init__(self, locations, data):
        self.locations = locations
        self.data = data

    def add_stop(self):
        index, string = int(self.data[1]), self.data[2]
        if index in range(len(self.locations)):
            self.locations = self.locations[:index] + string + self.locations[index:]
            return self.locations
        return False


class RemoveStop:

    def __init__(self, locations, data):
        self.locations = locations
        self.data = data

    def remove_stop(self):
        start_index, end_index = int(self.data[1]), int(self.data[2])
        if 0 <= start_index <= end_index < len(self.locations):
            self.locations = self.locations[:start_index] + self.locations[end_index + 1:]
            return self.locations
        return False


class Switch:

    def __init__(self, locations, data):
        self.locations = locations
        self.data = data

    def switching(self):
        old_stop, new_stop = self.data[1], self.data[2]
        if old_stop in self.locations:
            self.locations = self.locations.replace(old_stop, new_stop)
            return self.locations
        return False


class Actions:

    def __init__(self, destinations, some_input):
        self.destinations = destinations
        self.some_input = some_input

    def define_action(self):
        data = self.some_input.split(':')
        action = data[0]

        if action == 'Add Stop':
            add_stop = AddStop(self.destinations, data)
            return add_stop.add_stop()
        elif action == 'Remove Stop':
            remove_stop = RemoveStop(self.destinations, data)
            return remove_stop.remove_stop()
        elif action == 'Switch':
            switch_stop = Switch(self.destinations, data)
            return switch_stop.switching()
        else:
            return False


class Main:

    def __init__(self, destinations):
        self.destinations = destinations
        self.log = []

    def choose_destination(self):
        while True:
            input_data = input()
            if input_data == 'Travel':
                break

            data = Actions(self.destinations, input_data).define_action()
            if data is not False:
                self.destinations = data
                self.log.append(data)
            else:
                self.log.append(self.destinations)

    def printing(self):
        print(*self.log, sep='\n')
        print(f"Ready for world tour! Planned stops: {self.destinations}")


initial_locations = input()
output = Main(initial_locations)
output.choose_destination()
output.printing()

travel = input()

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
