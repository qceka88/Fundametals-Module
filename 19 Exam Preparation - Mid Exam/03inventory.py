items_list = input().split(', ')

while True:
    input_data = input()

    if input_data == 'Craft!':
        break

    command, item = input_data.split(' - ')

    if command == 'Collect':
        if item not in items_list:
            items_list.append(item)
    elif command == 'Drop':
        if item in items_list:
            items_list.remove(item)
    elif command == 'Combine Items':
        old_item, new_item = item.split(':')
        if old_item in items_list:
            old_index = items_list.index(old_item)
            items_list.insert(old_index + 1, new_item)
    elif command == 'Renew':
        if item in items_list:
            items_list.remove(item)
            items_list.append(item)

print(*items_list, sep=', ')



#################################### TASK CONDITION ############################
"""
                       3.	Inventory
Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2028#2.
As a young traveler, you gather items and craft new items.
Input / Constraints
You will receive a journal with some collecting items, 
separated with a comma and a space (", "). After that, until receiving "Craft!" 
you will be receiving different commands split by " - ":
•	"Collect - {item}" - you should add the given item to your inventory. 
If the item already exists, you should skip this line.
•	"Drop - {item}" - you should remove the item from your inventory if it exists.
•	"Combine Items - {old_item}:{new_item}" - you should check if 
the old item exists. If so, add the new item after the old one. 
Otherwise, ignore the command.
•	"Renew – {item}" – if the given item exists, 
you should change its position and put it last in your inventory.
Output
After receiving "Craft!" print the items in your inventory, separated by ", ".


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
