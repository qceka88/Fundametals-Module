phonebook_dict = {}

command = input()
while '-' in command:
    name, number = command.split('-')
    phonebook_dict[name] = number
    command = input()

loop_range = int(command)
for search in range(loop_range):
    name = input()
    if name not in phonebook_dict.keys():
        print(f"Contact {name} does not exist.")
    else:
        print(f"{name} -> {phonebook_dict[name]}")




#################################### TASK CONDITION ############################
"""
                              4.	Phonebook
Write a program that receives info from the console about people and their phone numbers.
Each entry should have a name and a number (both strings) separated by a "-". 
If you receive a name that already exists in the phonebook, update its number.
After filling the phonebook, you will receive a number – N. Your program should be 
able to perform a search of contact by name and print its details in the 
format: "{name} -> {number}". In case the contact isn't found, print: "Contact {name} does not exist."


____________________________________________________________________________________________
Example_01

Input
Adam-0888080808
2
Mery
Adam

Output
Contact Mery does not exist.
Adam -> 0888080808


____________________________________________________________________________________________
Example_02

Input
Adam-+359888001122
Ralf-666
George-5559393
Silvester-02/987665544
4
Silvester
silvester
Rolf
Ralf

Output
Silvester -> 02/987665544
Contact silvester does not exist.
Contact Rolf does not exist.
Ralf -> 666

"""
