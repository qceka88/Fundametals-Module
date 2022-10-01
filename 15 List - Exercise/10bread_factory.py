day_events = input().split('|')

total_energy = 100
total_coins = 100

handle_event = True

for event in day_events:
    input_data = event.split('-')
    command = input_data[0]
    number = int(input_data[1])

    if command == 'rest':
        current_energy = total_energy
        total_energy += number
        if total_energy > 100:
            total_energy = 100
        gained_energy = total_energy - current_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {total_energy}.")
    elif command == 'order':
        if total_energy - 30 >= 0:
            total_energy -= 30
            total_coins += number
            print(f"You earned {number} coins.")
        else:
            total_energy += 50
            print("You had to rest!")
    else:
        if total_coins - number >= 0:
            total_coins -= number
            print(f"You bought {command}.")
        else:
            handle_event = False
            print(f"Closed! Cannot afford {command}.")
            break

if handle_event:
    print("Day completed!")
    print(f"Coins: {total_coins}")
    print(f"Energy: {total_energy}")


#################################### TASK CONDITION ############################
"""
                  10.	* Bread Factory
As a young baker, you are baking the bread out of the bakery. 
You have initial energy 100 and initial coins 100
 You will be given a string representing the working day events. 
 Each event is separated with '|' (vertical bar): "event1|event2| … eventN"
Each event contains an event name or an ingredient and a number,
 separated by a dash ("{event/ingredient}-{number}")
•	If the event is "rest":
o	You gain energy (the number in the second part). Note: your energy cannot
 exceed your initial energy (100). Print: "You gained {gained_energy} energy.". 
o	After that, print your current energy: "Current energy: {current_energy}.".
•	If the event is "order": 
o	You've earned some coins (the number in the second part). 
o	Each time you get an order, your energy decreases by 30 points.
	If you have the energy to complete the order, print: "You earned {earned} coins.".
	Otherwise, skip the order and gain 50 energy points. Print: "You had to rest!".
•	In any other case, you have an ingredient you should buy.
 The second part of the event contains the coins you should spend. 
o	If you have enough money, you should buy the ingredient and print:
"You bought {ingredient}."
o	Otherwise, print "Closed! Cannot afford {ingredient}." and your bakery rush is over. 
If you managed to handle all events throughout the day, print on the following 3 lines: 
"Day completed!"
"Coins: {coins}"
"Energy: {energy}"
Input / Constraints
You will receive a string representing the working day events,
 separated with '|' (vertical bar) in the format:
"event1|event2| … eventN".
Each event contains an event name or an ingredient and a number,
 separated by a dash in the format: "{event/ingredient}-{number}"
Output
Print the corresponding messages described above.


____________________________________________________________________________________________
Example_01

Input
rest-2|order-10|eggs-100|rest-10

Output
You gained 0 energy.Current energy: 100.
You earned 10 coins.
You bought eggs.
You gained 10 energy.
Current energy: 80.
Day completed!
Coins: 10
Energy: 80


____________________________________________________________________________________________
Example_02

Input
order-10|order-10|order-10|flour-100|order-100|oven-100|order-1000

Output
You earned 10 coins.
You earned 10 coins.
You earned 10 coins.
You bought flour.
You had to rest!	
Closed! Cannot afford oven.

"""