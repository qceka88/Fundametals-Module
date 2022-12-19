inventory = input().split(', ')

while True:
    command = input()
    if command == "Craft!":
        break
    input_data = command.split(' - ')
    order = input_data[0]
    item = input_data[1]
    if order == 'Collect':
        if item not in inventory:
            inventory.append(item)
    elif order == 'Drop':
        if item in inventory:
            inventory.remove(item)
    elif order == 'Combine Items':
        items = item.split(':')
        old_item = items[0]
        new_item = items[1]
        if old_item in inventory:
            old_index = inventory.index(old_item)
            inventory.insert(old_index +1 , new_item)
    elif order == 'Renew':
        if item in inventory:
            inventory.remove(item)
            inventory.append(item)

print(*inventory, sep=', ')

#################################### TASK CONDITION ############################
"""
                          Problem 3. Inventory
Problem for exam preparation for the Programming Fundamentals Course @SoftUni.
Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2028#2.

As a young traveler, you gather items and craft new items.
Input / Constraints
You will receive a journal with some collecting items, separated with a comma and a space (", ").
 After that, until receiving "Craft!" you will be receiving different commands split by " - ":
•	"Collect - {item}" - you should add the given item to your inventory. 
If the item already exists, you should skip this line.
•	"Drop - {item}" - you should remove the item from your inventory if it exists.
•	"Combine Items - {old_item}:{new_item}" - you should check if the old item exists. 
If so, add the new item after the old one. Otherwise, ignore the command.
•	"Renew – {item}" – if the given item exists, you should change its position and put it last in your inventory.
Output
After receiving "Craft!" print the items in your inventory, separated by ", ".
Examples


____________________________________________________________________________________________
Example_01

Input
Iron, Wood, Sword
Collect - Gold
Drop - Wood
Craft!


Output
Iron, Sword, Gold 

____________________________________________________________________________________________
Example_02

Input
Iron, Sword
Drop - Bronze
Combine Items - Sword:Bow
Renew - Iron
Craft!


Output
Sword, Bow, Iron

"""