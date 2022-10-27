class Party:

    def __init__(self, people=[]):
        self.people = people

    def invited_people(self, human):
        self.people.append(human)

    def going_names(self):
        return f'Going: {", ".join(self.people)}'

    def quantity_people(self):
        return f"Total: {len(self.people)}"


party = Party()

while True:
    command = input()
    if command == 'End':
        break

    name = command
    party.invited_people(name)

print(party.going_names())
print(party.quantity_people())


#################################### TASK CONDITION ############################
'''
                                  2.	Party
                                  
Create a class Party that only has an attribute people – empty list. 
The __init__ method should not accept any parameters. 
You will be given names of people (on separate lines) until you receive 
the command "End". Use the created class to solve this problem. 

After you receive the "End" command, print 2 lines:
•	"Going: {people}" - the people should be separated by comma and space ", ".
•	"Total: {total_people_going}"

Note: submit all of your code, including the class
_____________________________________________

Example_01

Input
Peter
John
Katy

Output
End	Going: Peter, John, Katy
Total: 3
____________________________________________
Example_02

Input
Sam
Eddy
Edd
Kris
End	

Output
Going: Sam, Eddy, Edd, Kris
Total: 4

'''
