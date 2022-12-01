##################################### variant 01 #####################################


number_of_cars = int(input())
cars_catalogue = {}

for next in range(number_of_cars):
    car, mileage, fuel = input().split('|')
    cars_catalogue[car] = {'odo_meter': int(mileage), 'fuel': int(fuel)}

while True:
    command = input()
    if command == 'Stop':
        break

    data = command.split(' : ')
    action, car = data[0], data[1]

    if action == 'Drive':
        distance = int(data[2])
        needed_fuel = int(data[3])
        if needed_fuel > cars_catalogue[car]['fuel']:
            print('Not enough fuel to make that ride')
        else:
            cars_catalogue[car]['fuel'] -= needed_fuel
            cars_catalogue[car]['odo_meter'] += distance
            print(f'{car} driven for {distance} kilometers. {needed_fuel} liters of fuel consumed.')
    elif action == 'Refuel':
        fuel = int(data[2])
        tank_capacity = 75
        if cars_catalogue[car]['fuel'] + fuel > tank_capacity:
            fuel = tank_capacity - cars_catalogue[car]['fuel']
        cars_catalogue[car]['fuel'] += fuel
        print(f'{car} refueled with {fuel} liters')
    elif action == 'Revert':
        kilometer = int(data[2])
        min_odo = 10000
        if cars_catalogue[car]['odo_meter'] - kilometer < min_odo:
            cars_catalogue[car]['odo_meter'] = min_odo
        else:
            cars_catalogue[car]['odo_meter'] -= kilometer
            print(f"{car} mileage decreased by {kilometer} kilometers")

    if cars_catalogue[car]['odo_meter'] > 100000:
        del cars_catalogue[car]
        print(f'Time to sell the {car}!')

for vehicle, info in cars_catalogue.items():
    print(f"{vehicle} -> Mileage: {info['odo_meter']} kms, Fuel in the tank: {info['fuel']} lt.")


##################################### variant 02 #####################################


class Drive:

    def __init__(self, cars_dict, some_data):
        self.cars_dict = cars_dict
        self.some_data = some_data
        self.message = ''

    def driving(self):
        car, distance, needed_fuel = self.some_data[1], int(self.some_data[2]), int(self.some_data[3])
        if needed_fuel > self.cars_dict[car]['fuel']:
            self.message += 'Not enough fuel to make that ride\n'
        else:
            self.cars_dict[car]['fuel'] -= needed_fuel
            self.cars_dict[car]['odo_meter'] += distance
            self.message += f'{car} driven for {distance} kilometers. {needed_fuel} liters of fuel consumed.\n'

    def return_data(self):
        return self.message, self.cars_dict


class CheckOdoMeter:

    def __init__(self, cars_dict, some_data):
        self.cars_dict = cars_dict
        self.some_data = some_data
        self.message = ''

    def check_odo(self):
        max_mileage = 100000
        car = self.some_data[1]
        if self.cars_dict[car]['odo_meter'] > max_mileage:
            del self.cars_dict[car]
            self.message += f'Time to sell the {car}!\n'

    def return_data(self):
        return self.message, self.cars_dict


class Refuel:

    def __init__(self, cars_dict, some_data):
        self.cars_dict = cars_dict
        self.some_data = some_data
        self.message = ''

    def refueling(self):
        car, fuel = self.some_data[1], int(self.some_data[2]),
        tank_capacity = 75
        if self.cars_dict[car]['fuel'] + fuel > tank_capacity:
            fuel = tank_capacity - self.cars_dict[car]['fuel']
        self.cars_dict[car]['fuel'] += fuel
        self.message += f'{car} refueled with {fuel} liters\n'

    def return_data(self):
        return self.message, self.cars_dict


class Revert:

    def __init__(self, cars_dict, some_data):
        self.cars_dict = cars_dict
        self.some_data = some_data
        self.message = ''

    def reverting(self):
        car, amount_kilometer = self.some_data[1], int(self.some_data[2]),
        min_odo = 10000
        if self.cars_dict[car]['odo_meter'] - amount_kilometer < min_odo:
            self.cars_dict[car]['odo_meter'] = min_odo
        else:
            self.cars_dict[car]['odo_meter'] -= amount_kilometer
            self.message += f"{car} mileage decreased by {amount_kilometer} kilometers\n"

    def return_data(self):
        return self.message, self.cars_dict


class Actions:

    def __init__(self, cars_dict, some_input):
        self.cars_dict = cars_dict
        self.some_input = some_input
        self.log = ''

    def define_action_with_car(self):
        data = self.some_input.split(' : ')
        action = data[0]
        if action == 'Drive':
            drive_object = Drive(self.cars_dict, data)
            drive_object.driving()
            self.log += drive_object.return_data()[0]
            self.cars_dict = drive_object.return_data()[1]
            used_car = CheckOdoMeter(self.cars_dict, data)
            used_car.check_odo()
            if used_car.return_data() is not False:
                self.log += used_car.return_data()[0]
                self.cars_dict = used_car.return_data()[1]
        elif action == 'Refuel':
            refuel_object = Refuel(self.cars_dict, data)
            refuel_object.refueling()
            self.log += refuel_object.return_data()[0]
            self.cars_dict = refuel_object.return_data()[1]
        elif action == 'Revert':
            revert_object = Revert(self.cars_dict, data)
            revert_object.reverting()
            self.log += revert_object.return_data()[0]
            self.cars_dict = revert_object.return_data()[1]

    def return_to_main(self):
        return self.log, self.cars_dict


class Main:

    def __init__(self):
        self.catalogue = {}
        self.log_file = ''

    def garage_fill(self):
        number_of_cars = int(input())
        for next in range(number_of_cars):
            car, mileage, fuel = input().split('|')
            self.catalogue[car] = {'odo_meter': int(mileage), 'fuel': int(fuel)}

    def use_cars(self):
        while True:
            command = input()
            if command == 'Stop':
                break
            car_action = Actions(self.catalogue, command)
            car_action.define_action_with_car()
            self.log_file += car_action.return_to_main()[0]
            self.catalogue = car_action.return_to_main()[1]

    def final_catalogue(self):
        for vehicle, info in self.catalogue.items():
            self.log_file += f"{vehicle} -> Mileage: {info['odo_meter']} kms, Fuel in the tank: {info['fuel']} lt.\n"

    def __repr__(self):
        return f'{self.log_file}'


output = Main()
output.garage_fill()
output.use_cars()
output.final_catalogue()
print(output)


#################################### TASK CONDITION ############################
"""
                             Problem 3 - Need for Speed III
Problem for exam preparation for the Programming Fundamentals Course @SoftUni.
Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2307#2.

You have just bought the latest and greatest computer game – Need for Seed III. 
Pick your favorite cars and drive them all you want! We know that you can't wait to start playing.
On the first line of the standard input, you will receive an 
integer n – the number of cars that you can obtain. On the next n lines, 
the cars themselves will follow with their mileage and fuel available, separated by "|" in the following format:
"{car}|{mileage}|{fuel}"
Then, you will be receiving different commands, each on a new line, 
separated by " : ", until the "Stop" command is given:
•	"Drive : {car} : {distance} : {fuel}":
o	You need to drive the given distance, and you will need the 
given fuel to do that. If the car doesn't have enough fuel,
 print: "Not enough fuel to make that ride"
o	If the car has the required fuel available in the tank, 
ncrease its mileage with the given distance, decrease its fuel with the given fuel, and print: 
"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed."
o	You like driving new cars only, so if a car's mileage reaches 100 000 km, 
remove it from the collection(s) and print: "Time to sell the {car}!"
•	"Refuel : {car} : {fuel}":
o	Refill the tank of your car. 
o	Each tank can hold a maximum of 75 liters of fuel, so if the given amount
of fuel is more than you can fit in the tank, take only what is required to fill it up. 
o	Print a message in the following format: "{car} refueled with {fuel} liters"
•	"Revert : {car} : {kilometers}":
o	Decrease the mileage of the given car with the given kilometers and print 
the kilometers you have decreased it with in the following format:
"{car} mileage decreased by {amount reverted} kilometers"
o	If the mileage becomes less than 10 000km after it is decreased, 
just set it to 10 000km and 
DO NOT print anything.
Upon receiving the "Stop" command, you need to print all cars in your possession in the following format:
"{car} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt."
Input/Constraints
•	The mileage and fuel of the cars will be valid, 32-bit integers, and will never be negative.
•	The fuel and distance amounts in the commands will never be negative.
•	The car names in the commands will always be valid cars in your possession.
Output
•	All the output messages with the appropriate formats are described in the problem description.

____________________________________________________________________________________________
Example_01

Input
3
Audi A6|38000|62
Mercedes CLS|11000|35
Volkswagen Passat CC|45678|5
Drive : Audi A6 : 543 : 47
Drive : Mercedes CLS : 94 : 11
Drive : Volkswagen Passat CC : 69 : 8
Refuel : Audi A6 : 50
Revert : Mercedes CLS : 500
Revert : Audi A6 : 30000
Stop

Output
Audi A6 driven for 543 kilometers. 47 liters of fuel consumed.
Mercedes CLS driven for 94 kilometers. 11 liters of fuel consumed.
Not enough fuel to make that ride
Audi A6 refueled with 50 liters
Mercedes CLS mileage decreased by 500 kilometers
Audi A6 -> Mileage: 10000 kms, Fuel in the tank: 65 lt.
Mercedes CLS -> Mileage: 10594 kms, Fuel in the tank: 24 lt.
Volkswagen Passat CC -> Mileage: 45678 kms, Fuel in the tank: 5 lt.


Explanation
After we receive the cars with their mileage and fuel,
we start driving them. When we get to "Drive : Volkswagen Passat CC : 69 : 8" command,
our program calculates that there is not enough fuel, and we print the appropriate message.
Then we refuel the Audi A6 with 50 l of fuel and Revert the Mercedes with 500 kilometers.
When we receive the "Revert : Audi A6 : 30000", we set its mileage to 10000 km, 
because if the current mileage of the Audi is 38543 kms and if we subtract 30000 from it,
we receive 8543 kms, which is less than 10000 kms.
After all the commands, we print our current collection of cars with their 
current mileage and current fuel.

____________________________________________________________________________________________
Example_02

Input
Lamborghini Veneno|11111|74
Bugatti Veyron|12345|67
Koenigsegg CCXR|67890|12
Aston Martin Valkryie|99900|50
Drive : Koenigsegg CCXR : 382 : 82
Drive : Aston Martin Valkryie : 99 : 23
Drive : Aston Martin Valkryie : 2 : 1
Refuel : Lamborghini Veneno : 40
Revert : Bugatti Veyron : 2000
Stop

Output
Not enough fuel to make that ride
Aston Martin Valkryie driven for 99 kilometers. 23 liters of fuel consumed.
Aston Martin Valkryie driven for 2 kilometers. 1 liters of fuel consumed.
Time to sell the Aston Martin Valkryie!
Lamborghini Veneno refueled with 1 liters
Bugatti Veyron mileage decreased by 2000 kilometers
Lamborghini Veneno -> Mileage: 11111 kms, Fuel in the tank: 75 lt.
Bugatti Veyron -> Mileage: 10345 kms, Fuel in the tank: 67 lt.
Koenigsegg CCXR -> Mileage: 67890 kms, Fuel in the tank: 12 lt.

"""