def drive_action(cars_info, car, input_data):
    max_odo_limit = 100000
    distance = int(input_data[2])
    fuel = int(input_data[3])
    if cars_info[car]['fuel'] - fuel < 0:
        print("Not enough fuel to make that ride")
    else:
        cars_info[car]['fuel'] -= fuel
        print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        cars_info[car]['odo'] += distance
    if cars_info[car]['odo'] >= max_odo_limit:
        print(f"Time to sell the {car}!")
        del cars_info[car]
    return cars_info


def refuel_action(cars_info, car, input_data):
    tank_capacity = 75
    current_refill = int(input_data[2])
    if cars_info[car]['fuel'] + current_refill > tank_capacity:
        current_refill = tank_capacity - cars_info[car]['fuel']
        cars_info[car]['fuel'] = 75
    else:
        cars_info[car]['fuel'] += current_refill
    print(f"{car} refueled with {current_refill} liters")

    return cars_info


def revert_action(cars_info, car, input_data):
    min_odo_limit = 10000
    kilometers = int(input_data[2])
    cars_info[car]['odo'] -= kilometers
    if cars_info[car]['odo'] < min_odo_limit:
        cars_info[car]['odo'] = 10000
    else:
        print(f"{car} mileage decreased by {kilometers} kilometers")
    return cars_info


cars_quantity = int(input())
garage = {}

for car_number in range(cars_quantity):
    car, odometer, fuel = input().split('|')
    garage[car] = {'odo': int(odometer), 'fuel': int(fuel)}

command = input()

while command != 'Stop':
    data = command.split(' : ')
    action = data[0]
    vehicle = data[1]

    if action == 'Drive':
        garage = drive_action(garage, vehicle, data)
    elif action == 'Refuel':
        garage = refuel_action(garage, vehicle, data)
    elif action == 'Revert':
        garage = revert_action(garage, vehicle, data)

    command = input()

for car, info in garage.items():
    print(f"{car} -> Mileage: {info['odo']} kms, Fuel in the tank: {info['fuel']} lt.")

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