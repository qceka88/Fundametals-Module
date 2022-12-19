def rate_action(plants_dict, plant_name, rating):
    if 'rating' not in plants_dict[plant_name]:
        plants_dict[plant_name].setdefault('rating', [])
    plants_dict[plant_name]['rating'].append(int(rating))
    return plants_dict


def update_action(plants_dict, plant_name, rarity):
    plants_dict[plant_name]['rarity'] = int(rarity)
    return plants_dict


def reset_action(plants_dict, plant_name):
    del plants_dict[plant_name]['rating']
    return plants_dict


number_of_plants = int(input())

plants_data = {}

for plant_input in range(number_of_plants):
    plant, rarity = input().split('<->')
    plants_data[plant] = {'rarity': int(rarity)}

while True:
    command = input().split(': ')

    if "Exhibition" in command:
        break

    action = command[0]
    data = command[1]

    if ' - ' in data:
        name, number = data.split(' - ')
    else:
        name = data

    if name not in plants_data:
        print("error")
    elif action == 'Rate':
        plants_data = rate_action(plants_data, name, number)
    elif action == 'Update':
        plants_data = update_action(plants_data, name, number)
    elif action == 'Reset':
        plants_data = reset_action(plants_data, name)

print('Plants for the exhibition:')

for plant_name, plant_info in plants_data.items():
    rarity = plant_info["rarity"]
    if 'rating' not in plant_info:
        avverage_rating = 0
    else:
        avverage_rating = sum(plant_info['rating']) / len(plant_info['rating'])
    print(f'- {plant_name}; Rarity: {rarity}; Rating: {avverage_rating:.2f}')

#################################### TASK CONDITION ############################
"""
                       Problem 3 - Plant Discovery
Problem for exam preparation for the Programming Fundamentals Course @SoftUni.
Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2518#2.

You have now returned from your world tour. On your way, 
you have discovered some new plants, and you want to gather some 
information about them and create an exhibition to see which plant is highest rated.
On the first line, you will receive a number n. 
On the next n lines, you will be given some information about 
the plants that you have discovered in the format: "{plant}<->{rarity}". 
Store that information because you will need it later. 
If you receive a plant more than once, update its rarity.
After that, until you receive the command "Exhibition", you will be given some of these commands:
•	"Rate: {plant} - {rating}" – add the given rating to the plant (store all ratings)
•	"Update: {plant} - {new_rarity}" – update the rarity of the plant with the new one
•	"Reset: {plant}" – remove all the ratings of the given plant
Note: If any given plant name is invalid, print "error"
After the command "Exhibition", print the information that you have about the plants in the following format:
"Plants for the exhibition:
- {plant_name1}; Rarity: {rarity}; Rating: {average_rating}
- {plant_name2}; Rarity: {rarity}; Rating: {average_rating}
…
- {plant_nameN}; Rarity: {rarity}; Rating: {average_rating}"
The average rating should be formatted to the second decimal place.
Input / Constraints
•	You will receive the input as described above
•	JavaScript: you will receive a list of strings
Output
•	Print the information about all plants as described above

____________________________________________________________________________________________
Example_01

Input
3
Arnoldii<->4
Woodii<->7
Welwitschia<->2
Rate: Woodii - 10
Rate: Welwitschia - 7
Rate: Arnoldii - 3
Rate: Woodii - 5
Update: Woodii - 5
Reset: Arnoldii
Exhibition

Output
Plants for the exhibition:
- Arnoldii; Rarity: 4; Rating: 0.00
- Woodii; Rarity: 5; Rating: 7.50
- Welwitschia; Rarity: 2; Rating: 7.00

____________________________________________________________________________________________
Example_02

Input
2
Candelabra<->10
Oahu<->10
Rate: Oahu - 7
Rate: Candelabra - 6
Exhibition

Output
Plants for the exhibition:
- Candelabra; Rarity: 10; Rating: 6.00
- Oahu; Rarity: 10; Rating: 7.00

"""