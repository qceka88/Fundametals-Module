class Converting:

    def __init__(self, some_dict):
        self.some_dict = some_dict
        self.some_list_with_dicts = []

    def dict_to_list(self):
        for some_color, some_dwarfs in self.some_dict.items():
            for some_name, some_physics in some_dwarfs.items():
                self.some_list_with_dicts.append(
                    {'length': len(some_dwarfs), 'physics': some_physics, 'name': some_name, 'color': some_color})

        return self.some_list_with_dicts


class DwarfsDict:

    def __init__(self, input_dict):
        self.input_dict = input_dict

    def transofrmers(self):
        some_list = Converting(self.input_dict)
        return some_list.dict_to_list()

    def printing(self):
        for dwarf in sorted(self.transofrmers(), key=lambda x: (x["physics"], x["length"]), reverse=True):
            print(f'({dwarf["color"]}) {dwarf["name"]} <-> {dwarf["physics"]}')


def fill_dict_with_data(dict_with_dwarfs, some_data):
    name, color, physics = some_data.split(' <:> ')
    if color not in dict_with_dwarfs:
        dict_with_dwarfs[color] = {}
    if name not in dict_with_dwarfs[color]:
        dict_with_dwarfs[color][name] = 0
    if int(physics) > dict_with_dwarfs[color][name]:
        dict_with_dwarfs[color][name] = int(physics)

    return dict_with_dwarfs


dwarfs_data_dict = {}
while True:
    command = input()
    if command == 'Once upon a time':
        break

    dwarfs_data_dict = fill_dict_with_data(dwarfs_data_dict, command)

output = DwarfsDict(dwarfs_data_dict)
output.printing()



#################################### TASK CONDITION ############################
"""
                              4.	Snow White
Snow White loves her dwarfs, but there are so many, and she doesn't know how to 
order them. Does she order them by name? Or by color of their hat? Or by physics? 
She can't decide, so it's up to you to write a program that does it for her.
You will be receiving several input lines which contain data about each dwarf in the following format:
{dwarf_name} <:> {dwarf_hat_color} <:> {dwarf_physics}
The "dwarf_name" and the "dwarf_hat_color" are strings. The "dwarf_physics" is an integer.
You must store the data about the dwarfs in your program. There are several rules though:
•	If 2 dwarfs have the same name but different color, they should be considered 
different dwarfs, and you should store them both.
•	If 2 dwarfs have the same name and the same color, store the one with the higher physics.
When you receive the command "Once upon a time", the input ends. You must order the 
dwarfs by physics in descending order and then by total count of dwarfs with the same hat color in descending order. 
Then you must print them all.
Input
•	The input will consist of several input lines, containing dwarf data in the format, specified above.
•	The input ends when you receive the command "Once upon a time". 
Output
•	As output, you must print the dwarfs, ordered in the way, specified above.
•	The output format is: "({hat_color}) {name} <-> {physics}"
Constraints
•	The "dwarf_name" will be a string which may contain any ASCII character except ' ' (space), '<', ':', '>'.
•	The "dwarf_hat_color" will be a string which may contain any ASCII character except ' ' (space), '<', ':', '>'.
•	The "dwarf_physics" will be an integer in range [0, 231 – 1].
•	There will be no invalid input lines.
•	If all sorting criteria fail, the order should be by order of input.
•	Allowed working time / memory: 100ms / 16MB.

____________________________________________________________________________________________
Example_01

Input
Peter <:> Red <:> 2000
Teodor <:> Blue <:> 1000
George <:> Green <:> 1000
Simon <:> Yellow <:> 4500
Dopey <:> Simon <:> 1000
Once upon a time	

Output
(Yellow) Simon <-> 4500
(Red) Peter <-> 2000
(Blue) Teodor <-> 1000
(Green) George <-> 1000
(Simon) Dopey <-> 1000

____________________________________________________________________________________________
Example_02

Input
Grumpy <:> Red <:> 5000
Grumpy <:> Blue <:> 10000
Grumpy <:> Red <:> 10000
Happy <:> Blue <:> 10000
Once upon a time	

Output
(Blue) Grumpy <-> 10000
(Blue) Happy <-> 10000
(Red) Grumpy <-> 10000


"""
