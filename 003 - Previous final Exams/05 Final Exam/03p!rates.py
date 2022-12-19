def plunder(city_dict, city, input_data):
    people = int(input_data[2])
    gold = int(input_data[3])
    city_dict[city]['population'] -= people
    city_dict[city]['gold'] -= gold
    print(f"{city} plundered! {gold} gold stolen, {people} citizens killed.")
    if city_dict[city]['gold'] == 0 or city_dict[city]['population'] == 0:
        print(f"{city} has been wiped off the map!")
        del city_dict[city]

    return city_dict


def prosper(city_dict, city, input_data):
    gold = int(input_data[2])
    if gold < 0:
        print("Gold added cannot be a negative number!")
    else:
        city_dict[city]['gold'] += gold
        print(f"{gold} gold added to the city treasury. {city} now has {city_dict[city]['gold']} gold.")
    return city_dict


cities = {}

while True:
    command = input()
    if command == 'Sail':
        break
    town, population, gold = command.split('||')
    if town not in cities:
        cities[town] = {'population': 0, 'gold': 0}
    cities[town]['population'] += int(population)
    cities[town]['gold'] += int(gold)

while True:
    input_line = input()
    if input_line == 'End':
        break

    data = input_line.split('=>')
    action = data[0]
    town = data[1]

    if action == 'Plunder':
        cities = plunder(cities, town, data)
    elif action == 'Prosper':
        cities = prosper(cities, town, data)

if len(cities) > 0:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for town, wealth in cities.items():
        people = wealth['population']
        gold = wealth['gold']
        print(f'{town} -> Population: {people} citizens, Gold: {gold} kg')
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")

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