from collections import defaultdict

chest = defaultdict(int)
command = input()

while command != 'stop':
    quantity = int(input())
    current_resource = command
    chest[current_resource] += quantity
    command = input()

for resource, quantity in chest.items():
    print(f"{resource} -> {quantity}")




#################################### TASK CONDITION ############################
"""
2.	A Miner Task
You will be given a sequence of strings, each on a new line until 
you receive the "stop" command. Every odd line on the console 
represents a resource (e.g., Gold, Silver, Copper, and so on) 
and every even - quantity. Your task is to collect the resources and print them each on a new line.
Print the resources and their quantities in the following format:
"{resource} -> {quantity}"
The quantities will be in the range [1 … 2 000 000 000].


____________________________________________________________________________________________
Example_01

Input
Gold
155
Silver
10
Copper
17
stop

Output
Gold -> 155
Silver -> 10
Copper -> 17


____________________________________________________________________________________________
Example_02

Input
gold
155
silver
10
copper
17
gold
15
stop

Output
gold -> 170
silver -> 10
copper -> 17

"""
