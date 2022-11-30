##################################### variant 01 #####################################

number_of_plants = int(input())
plants_dict = {}

for input_plant in range(number_of_plants):
    name, rarity = input().split('<->')
    plants_dict[name] = {'rarity': int(rarity)}

while True:
    command = input().split(': ')
    if command[0] == 'Exhibition':
        break

    data = command[1].split(' - ')
    action = command[0]
    name = data[0]

    if name not in plants_dict:
        print('error')
    elif action == 'Rate':
        rating = int(data[1])
        if 'rating' not in plants_dict[name]:
            plants_dict[name]['rating'] = []
        plants_dict[name]['rating'].append(rating)
    elif action == 'Update':
        new_rarity = int(data[1])
        plants_dict[name]['rarity'] = new_rarity
    elif action == 'Reset':
        del plants_dict[name]['rating']

print('Plants for the exhibition:')

for plant_name, data in plants_dict.items():
    rarity = data['rarity']
    if 'rating' not in data:
        average_rating = 0
    else:
        average_rating = sum(data['rating']) / len(data['rating'])
    print(f'- {plant_name}; Rarity: {rarity}; Rating: {average_rating:.2f}')

##################################### variant 02 #####################################

class Rating:

    def __init__(self, some_info, some_name, dict_plants):
        self.some_info = some_info
        self.some_name = some_name
        self.dict_plants = dict_plants

    def add_rating(self):
        rating = int(self.some_info[1])
        if 'rating' not in self.dict_plants[self.some_name]:
            self.dict_plants[self.some_name]['rating'] = []
        self.dict_plants[self.some_name]['rating'].append(rating)

    def return_data(self):
        return self.dict_plants


class Update:

    def __init__(self, some_info, some_name, dict_plants):
        self.some_info = some_info
        self.some_name = some_name
        self.dict_plants = dict_plants

    def update_rarity(self):
        new_rarity = int(self.some_info[1])
        self.dict_plants[self.some_name]['rarity'] = new_rarity

    def return_data(self):
        return self.dict_plants


class Reset:

    def __init__(self, some_name, dict_plants):
        self.some_name = some_name
        self.dict_plants = dict_plants

    def reseting(self):
        del self.dict_plants[self.some_name]['rating']

    def return_data(self):
        return self.dict_plants


class Actions:

    def __init__(self, some_data, some_dict):
        self.some_data = some_data
        self.some_dict = some_dict

    def define_action(self):
        action, data = self.some_data.split(': ')
        info = data.split(' - ')
        name = info[0]

        if name not in self.some_dict:
            return False
        elif action == 'Rate':
            rate = Rating(info, name, self.some_dict)
            rate.add_rating()
            return rate.return_data()
        elif action == 'Update':
            update = Update(info, name, self.some_dict)
            update.update_rarity()
            return update.return_data()
        elif action == 'Reset':
            reset = Reset(name, self.some_dict)
            reset.reseting()
            return reset.return_data()


class Main:

    def __init__(self):
        self.plants_book = {}
        self.log_file = 'Plants for the exhibition:'

    def fill_dict(self):
        input_number = int(input())
        for input_plant in range(input_number):
            name, rarity = input().split('<->')
            self.plants_book[name] = {'rarity': int(rarity)}

    def discovery(self):
        while True:
            input_command = input()
            if input_command == 'Exhibition':
                break
            action_object = Actions(input_command, self.plants_book).define_action()
            if action_object is False:
                print('error')
            else:
                self.plants_book = action_object

    def classify_information(self):
        for plant_name, data in self.plants_book.items():
            rarity = data['rarity']
            if 'rating' not in data:
                average_rating = 0
            else:
                average_rating = sum(data['rating']) / len(data['rating'])
            self.log_file += f'\n - {plant_name}; Rarity: {rarity}; Rating: {average_rating:.2f}'

    def __repr__(self):
        return f'{self.log_file}'


output = Main()
output.fill_dict()
output.discovery()
output.classify_information()

print(output)

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