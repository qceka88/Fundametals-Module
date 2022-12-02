##################################### variant 01 #####################################
town_dict = {}

while True:
    command = input()
    if command == 'Sail':
        break
    city_name, population, gold = command.split('||')

    if city_name not in town_dict:
        town_dict[city_name] = {'people': 0, 'gold': 0}
    town_dict[city_name]['people'] += int(population)
    town_dict[city_name]['gold'] += int(gold)

while True:
    input_line = input()
    if input_line == 'End':
        break

    data = input_line.split('=>')
    action, town = data[0], data[1]

    if action == 'Plunder':
        people, gold = int(data[2]), int(data[3])
        town_dict[town]['people'] -= people
        town_dict[town]['gold'] -= gold
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        if town_dict[town]['people'] == 0 or town_dict[town]['gold'] == 0:
            del town_dict[town]
            print(f"{town} has been wiped off the map!")
    elif action == 'Prosper':
        income_gold = int(data[2])
        if income_gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            town_dict[town]['gold'] += income_gold
            print(f"{income_gold} gold added to the city treasury. {town} now has {town_dict[town]['gold']} gold.")

count = len(town_dict)

if count > 0:
    print(f'Ahoy, Captain! There are {count} wealthy settlements to go to:')
    for town_name, info in town_dict.items():
        people = info['people']
        gold = info['gold']
        print(f'{town_name} -> Population: {people} citizens, Gold: {gold} kg')
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")

##################################### variant 02 #####################################

class Plunder:

    def __init__(self, some_dict, some_input):
        self.some_dict = some_dict
        self.some_input = some_input
        self.message = ''

    def plundering_method(self):
        town, people, gold = self.some_input[1], int(self.some_input[2]), int(self.some_input[3])
        self.some_dict[town]['people'] -= people
        self.some_dict[town]['gold'] -= gold
        self.message += f"{town} plundered! {gold} gold stolen, {people} citizens killed.\n"

    def return_data(self):
        return self.some_dict, self.message


class CheckTown:

    def __init__(self, some_dict, some_input):
        self.some_dict = some_dict
        self.some_input = some_input
        self.message = ''

    def check_town_parameter(self):
        town = self.some_input[1]
        if self.some_dict[town]['people'] <= 0 or self.some_dict[town]['gold'] <= 0:
            del self.some_dict[town]
            self.message += f"{town} has been wiped off the map!\n"

    def return_data(self):
        return self.some_dict, self.message


class Prosper:

    def __init__(self, some_dict, some_input):
        self.some_dict = some_dict
        self.some_input = some_input
        self.message = ''

    def prosper_method(self):
        town, income_gold = self.some_input[1], int(self.some_input[2])
        if income_gold < 0:
            self.message += "Gold added cannot be a negative number!\n"
        else:
            self.some_dict[town]['gold'] += income_gold
            current_gold = self.some_dict[town]['gold']
            self.message += f"{income_gold} gold added to the city treasury. {town} now has {current_gold} gold.\n"

    def return_data(self):
        return self.some_dict, self.message


class Pirates:

    def __init__(self, some_dict, some_input):
        self.some_dict = some_dict
        self.some_input = some_input
        self.log = ''

    def define_action(self):
        data = self.some_input.split('=>')
        action = data[0]
        if action == 'Plunder':
            plunder_object = Plunder(self.some_dict, data)
            plunder_object.plundering_method()
            self.some_dict = plunder_object.return_data()[0]
            self.log += plunder_object.return_data()[1]
            check_parameter = CheckTown(self.some_dict, data)
            check_parameter.check_town_parameter()
            self.some_dict = check_parameter.return_data()[0]
            self.log += check_parameter.return_data()[1]
        elif action == 'Prosper':
            prosper_object = Prosper(self.some_dict, data)
            prosper_object.prosper_method()
            self.some_dict = prosper_object.return_data()[0]
            self.log += prosper_object.return_data()[1]

    def return_to_main(self):
        return self.some_dict, self.log


class DefineTowns:

    def __init__(self, some_dict, some_input):
        self.some_dict = some_dict
        self.some_input = some_input

    def fill_dict_with_towns(self):
        city_name, population, gold = self.some_input.split('||')
        if city_name not in self.some_dict:
            self.some_dict[city_name] = {'people': 0, 'gold': 0}
        self.some_dict[city_name]['people'] += int(population)
        self.some_dict[city_name]['gold'] += int(gold)

    def return_to_main(self):
        return self.some_dict


class Main:

    def __init__(self):
        self.towns_dict = {}
        self.log_file = ''

    def initial_towns(self):
        while True:
            input_command = input()
            if input_command == 'Sail':
                break
            town_ojbect = DefineTowns(self.towns_dict, input_command)
            town_ojbect.fill_dict_with_towns()
            self.towns_dict = town_ojbect.return_to_main()

    def pirating(self):
        while True:
            input_line = input()
            if input_line == 'End':
                break
            pirate_object = Pirates(self.towns_dict, input_line)
            pirate_object.define_action()
            self.towns_dict = pirate_object.return_to_main()[0]
            self.log_file += pirate_object.return_to_main()[1]

    def result(self):
        count = len(self.towns_dict)
        if count > 0:
            self.log_file += f'Ahoy, Captain! There are {count} wealthy settlements to go to:\n'
            for town_name, info in self.towns_dict.items():
                people = info['people']
                gold = info['gold']
                self.log_file += f'{town_name} -> Population: {people} citizens, Gold: {gold} kg\n'
        else:
            self.log_file += "Ahoy, Captain! All targets have been plundered and destroyed!"

    def __repr__(self):
        return f'{self.log_file}'


output = Main()
output.initial_towns()
output.pirating()
output.result()
print(output)


#################################### TASK CONDITION ############################
"""
                    Problem 3 - P!rates
Problem for exam preparation for the Programming Fundamentals Course @SoftUni.
Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2302#2.

Anno 1681. The Caribbean. The golden age of piracy. 
You are a well-known pirate captain by the name of Jack Daniels. 
Together with your comrades Jim (Beam) and Johnny (Walker), 
you have been roaming the seas, looking for gold and treasure… 
and the occasional killing, of course. Go ahead, target 
some wealthy settlements and show them the pirate's way!
Until the "Sail" command is given, you will be receiving:
•	You and your crew have targeted cities, with their population and gold, separated by "||".
•	If you receive a city that has already been received, 
you have to increase the population and gold with the given values.
After the "Sail" command, you will start receiving lines of text 
representing events until the "End" command is given. 
Events will be in the following format:
•	"Plunder=>{town}=>{people}=>{gold}"
o	You have successfully attacked and plundered the town, killing 
the given number of people and stealing the respective amount of gold. 
o	For every town you attack print this message: 
"{town} plundered! {gold} gold stolen, {people} citizens killed."
o	If any of those two values (population or gold) reaches zero, the town is disbanded.
	You need to remove it from your collection of targeted 
cities and print the following message: "{town} has been wiped off the map!"
o	There will be no case of receiving more people or gold than there is in the city.
•	"Prosper=>{town}=>{gold}"
o	There has been dramatic economic growth in the given city, 
increasing its treasury by the given amount of gold.
o	The gold amount can be a negative number, so be careful. 
If a negative amount of gold is given, print: "Gold added cannot be a 
negative number!" and ignore the command.
o	If the given gold is a valid amount, increase the town's gold reserves 
by the respective amount and print the following message: 
"{gold added} gold added to the city treasury. {town} now has {total gold} gold."
Input
•	On the first lines, until the "Sail" command, you will be receiving 
strings representing the cities with their gold and population, separated by "||"
•	On the following lines, until the "End" command, you will be receiving 
strings representing the actions described above, separated by "=>"
Output
•	After receiving the "End" command, if there are any existing settlements 
on your list of targets, you need to print all of them, in the following format:
"Ahoy, Captain! There are {count} wealthy settlements to go to:
{town1} -> Population: {people} citizens, Gold: {gold} kg
{town2} -> Population: {people} citizens, Gold: {gold} kg
   …
{town…n} -> Population: {people} citizens, Gold: {gold} kg"
•	If there are no settlements left to plunder, print:
"Ahoy, Captain! All targets have been plundered and destroyed!"
Constraints
•	The initial population and gold of the settlements will be valid 32-bit integers, 
never negative, or exceed the respective limits.
•	The town names in the events will always be valid towns that should be on your list.


____________________________________________________________________________________________
Example_01

Input
Tortuga||345000||1250
Santo Domingo||240000||630
Havana||410000||1100
Sail
Plunder=>Tortuga=>75000=>380
Prosper=>Santo Domingo=>180
End

Output
Tortuga plundered! 380 gold stolen, 75000 citizens killed.
180 gold added to the city treasury. Santo Domingo now has 810 gold.
Ahoy, Captain! There are 3 wealthy settlements to go to:
Tortuga -> Population: 270000 citizens, Gold: 870 kg
Santo Domingo -> Population: 240000 citizens, Gold: 810 kg
Havana -> Population: 410000 citizens, Gold: 1100 kg

____________________________________________________________________________________________
Example_02

Input
Nassau||95000||1000
San Juan||930000||1250
Campeche||270000||690
Port Royal||320000||1000
Port Royal||100000||2000
Sail
Prosper=>Port Royal=>-200
Plunder=>Nassau=>94000=>750
Plunder=>Nassau=>1000=>150
Plunder=>Campeche=>150000=>690
End

Output
Gold added cannot be a negative number!
Nassau plundered! 750 gold stolen, 94000 citizens killed.
Nassau plundered! 150 gold stolen, 1000 citizens killed.
Nassau has been wiped off the map!
Campeche plundered! 690 gold stolen, 150000 citizens killed.
Campeche has been wiped off the map!
Ahoy, Captain! There are 2 wealthy settlements to go to:
San Juan -> Population: 930000 citizens, Gold: 1250 kg
Port Royal -> Population: 420000 citizens, Gold: 3000 kg

"""