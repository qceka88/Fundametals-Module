tail = input()
body = input()
head = input()

strange_zoo = [tail, body, head]
strange_zoo[0], strange_zoo[-1] = strange_zoo[-1], strange_zoo[0]
print(strange_zoo)



#################################### TASK CONDITION ############################
"""
                    1.	Strange Zoo
You are at the zoo, and the meerkats look strange. 
You will receive 3 strings on separate lines, representing the tail, 
the body, and the head of an animal in that order. Your task is to re-arrange 
the elements in a list so that the animal looks normal again:
•	On the first position is the head;
•	On the second position is the body;
•	On the last one is the tail.


____________________________________________________________________________________________
Example_01

Input
my tail
my body seems on place
my head is on the wrong end!

Output
['my head is on the wrong end!', 'my body seems on place', 'my tail']


____________________________________________________________________________________________
Example_02

Input

tail
body
head

Output
['head', 'body', 'tail']


____________________________________________________________________________________________
Example_03

Input
T
B
H

Output
['H', 'B', 'T']

"""
