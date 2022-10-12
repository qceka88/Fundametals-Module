wagon_number = [0 for i in range(int(input()))]

while True:
    command = input()
    if command == 'End':
        print(wagon_number)
        break

    input_data = command.split()
    order = input_data[0]
    index = int(input_data[1])

    if order == 'add':
        people = index
        wagon_number[-1] += people
    elif order == 'insert':
        people = int(input_data[2])
        wagon_number[index] += people
    elif order == 'leave':
        people = int(input_data[2])
        wagon_number[index] -= people




#################################### TASK CONDITION ############################
"""
                            2.	Trains
You will receive a number representing the number of wagons a train has. 
Create a list (train) with the given length containing only zeros. 
Until you receive the command "End", you will receive some of the following commands:
•	"add {people}" – you should add the number of people in the last wagon
•	"insert {index} {people}" - you should add the number of 
people at the given wagon
•	"leave {index} {people}" - you should remove the number of 
people from the wagon. There will be no case in which 
the people will be more than the count in the wagon.
There will be no case in which the index is invalid!
After you receive the "End" command print the train.


____________________________________________________________________________________________
Example_01

Input
3
add 20
insert 0 15
leave 0 5
End

Output
[10, 0, 20]


____________________________________________________________________________________________
Example_02

Input
5
add 10
add 20
insert 0 16
insert 1 44
leave 1 12
insert 2 100
insert 4 61
leave 4 1
add 15
End

Output
[16, 32, 100, 0, 105]

"""

