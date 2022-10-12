to_do_list = [0] * 10

command = input()

while command != 'End':
    input_data = command.split('-')
    importance = int(input_data[0]) - 1
    task = input_data[1]
    to_do_list.pop(importance)
    to_do_list.insert(importance, task)
    command = input()

print([to_do for to_do in to_do_list if to_do != 0])




#################################### TASK CONDITION ############################
"""
                               3.	To-do List
You will be receiving to-do notes until you get the command "End". 
The notes will be in the format: "{importance}-{note}". 
Return a list containing all to-do notes sorted by importance in ascending order. 
The importance value will always be an integer between 1 and 10 (inclusive).
Hint
•	Use the pop() and insert() methods.


____________________________________________________________________________________________
Example_01

Input
2-Walk the dog
1-Drink coffee
6-Dinner
5-Work
End

Output
['Drink coffee', 'Walk the dog', 'Work', 'Dinner']


____________________________________________________________________________________________
Example_02

Input
3-C
2-A
1-B
6-V
End

Output
['B', 'A', 'C', 'V']

"""

