university = {}
course = ''
while True:
    command = input()
    if ":" not in command:
        course = command.replace("_", ' ')
        break

    name, number, discipline = command.split(':')
    if discipline not in university:
        university[discipline] = []
    university[discipline].append(f'{name} - {number}')

print(*university[course], sep='\n')



#################################### TASK CONDITION ############################
"""
                     4.	Students
You will be receiving names of students, their ID, and a course of 
programming they have taken in the format "{name}:{ID}:{course}". 
On the last line, you will receive a name of a course in snake case 
lowercase letters. You should print only the information of the students 
who have taken the corresponding course in the format: "{name} - {ID}" on separate lines. 
Note: each student's ID will always be unique


____________________________________________________________________________________________
Example_01

Input
Peter:123:programming basics
John:5622:fundamentals
Maya:89:fundamentals
Lilly:633:fundamentals
fundamentals

Output
John - 5622
Maya - 89
Lilly - 633


____________________________________________________________________________________________
Example_02

Input
Alex:6:programming basics
Maria:7:programming basics
Kaloyan:9:advanced
Todor:10:fundamentals
programming_basics

Output
Alex - 6
Maria - 7

"""
