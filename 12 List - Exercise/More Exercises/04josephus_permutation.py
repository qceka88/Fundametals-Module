############################# variant 01 ################################
people_list = input().split()
number = int(input())

permutation = []
counter = 0
while len(people_list) > 0:
    for index, human in enumerate(people_list):
        counter += 1
        if counter % number == 0:
            permutation.append(human)
            people_list.pop(human)
            counter = 1
            if len(people_list) <= index:
                counter = 0

print('[' + ','.join(permutation) + ']')
############################# variant 02 ################################
people_list = input().split()
number = int(input())

permutation = []
human_index = 0
counter = 0
while len(people_list) > 0:
    counter += 1
    if counter % number == 0:
        permutation.append(people_list[human_index])
        people_list.pop(human_index)
    else:
        human_index += 1
    if human_index >= len(people_list):
        human_index = 0
print('[' + ','.join(permutation) + ']')

#################################### TASK CONDITION ############################
"""
                     4.	Josephus Permutation
This problem takes its name from arguably the most important event 
in the life of the ancient historian Josephus. According to his tale, he and his 
40 soldiers were trapped in a cave by the Romans during a siege.
Refusing to surrender to the enemy, they instead opted for mass suicide, with a twist: 
they formed a circle and proceeded to kill one man of every three until 
one last man was left (and that it was supposed to kill himself to end the act). 
Well, Josephus and another man were the last, and, as we now know every detail of the story, 
you may have correctly guessed that they did not precisely follow through with the original idea.
You are now to create a program that prints a Josephus permutation, receiving two lines of code:
•	the list itself - numbers separated by a single space representing the people in the circle
•	a number k
People are standing in a circle waiting to be executed. Counting begins from the first one
in the circle and proceeds from left to right. After a specified number of people are skipped,
the k person is executed. The procedure is repeated with the remaining people, 
starting with the next person, going in the same direction, and skipping the same number of people until no one remains.
Print the people by order of executions in the format: "[{executed1},{executed2}, … {executedN}]"


____________________________________________________________________________________________
Example_01

Input
1 2 3 4 5 6 7
3

Output
[3,6,2,7,5,1,4]	

Explanation
[1,2,3,4,5,6,7] - initial sequence
[1,2,4,5,6,7] => 3 is counted out and goes into the result [3]
[1,2,4,5,7] => 6 is counted out and goes into the result [3,6]
[1,4,5,7] => 2 is counted out and goes into the result [3,6,2]
[1,4,5] => 7 is counted out and goes into the result [3,6,2,7]
[1,4] => 5 is counted out and goes into the result [3,6,2,7,5]
[4] => 1 is counted out and goes into the result [3,6,2,7,5,1]
[] => 4 is counted out and goes into the result [3,6,2,7,5,1,4]


____________________________________________________________________________________________
Example_02

Input
10 5 65 104 1 0 2
8

Output
[10,65,0,1,5,2,104]

"""
