##########################  var 01 ###################################
input_line = input().split(' ')
food_dict = {}

for index in range(0, len(input_line), 2):
    food = input_line[index]
    quantity = input_line[index + 1]
    food_dict[food] = int(quantity)

print(food_dict)

##########################  var 02 ###################################

input_line = input().split()
dict_line = {input_line[i]: int(input_line[i+1]) for i in range(0, len(input_line), 2)}
print(dict_line)



#################################### TASK CONDITION ############################
"""
                           1.	Bakery
Your first task at your new job is to create a table of the stock 
in a bakery, and you really don't want to fail on your first day at work.
You will receive a single line containing some food (keys) and quantities (values). 
They will be separated by a single space (the first element is the key, 
the second – the value, and so on). Create a dictionary with all the 
keys and values and print it on the console.


____________________________________________________________________________________________
Example_01

Input
bread 10 butter 4 sugar 9 jam 12

Output
{'bread': 10, 'butter': 4, 'sugar': 9, 'jam': 12}


____________________________________________________________________________________________
Example_02

Input
eggs 3 sugar 7 salt 1 butter 3

Output
{'eggs': 3, 'sugar': 7, 'salt': 1, 'butter': 3}


"""
