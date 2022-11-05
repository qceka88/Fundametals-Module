from collections import defaultdict

submissions = defaultdict(int)
students = {}

while True:
    command = input()
    if command == 'exam finished':
        break

    input_data = command.split('-')
    name = input_data[0]
    language = input_data[1]

    if language == 'banned':
        for course, student_names in students.items():
            if name in student_names.keys():
                students[course].pop(name)
    else:
        submissions[language] += 1
        points = int(input_data[2])
        if language not in students.keys():
            students[language] = {}
        if name not in students[language]:
            students[language][name] = 0
        if students[language][name] < points:
            students[language][name] = points


print('Results:')
for course, users in students.items():
    for name, score in users.items():
        print(f"{name} | {score}")

print('Submissions:')
print('\n'.join(f'{language} - {count}' for language, count in submissions.items()))




#################################### TASK CONDITION ############################
"""
                      12.	*SoftUni Exam Results
Judge statistics on the last Programing Fundamentals exam were not 
working correctly, so you have the task of taking all the submissions 
and analyzing them properly. You should collect all the submissions and 
print the final results and statistics about each language in which the 
participants submitted their solutions.You will be receiving lines in the 
following format: "{username}-{language}-{points}" until you receive "exam finished". 
You should store each username and their submissions and points. 
If a student has two or more submissions for the same language, save only his maximum points.
You can receive a command to ban a user for cheating in the 
following format: "{username}-banned". In that case, you should remove the user 
from the contest but preserve his submissions in the total count of submissions for each language.
After receiving "exam finished", print each of the participants in the following format:
"Results:
{username1} | {points}
{username2} | {points}
…
{usernameN} | {points}"
After that, print each language used in the exam in the following format:
"Submissions:
{language1} - {submissions_count}
{language2} - {submissions_count}
…
{language3} - {submissions_count}"
Input / Constraints
Until you receive "exam finished" you will be receiving participant 
submissions in the following format: "{username}-{language}-{points}"
You can receive a ban command -> "{username}-banned"
The points of the participant will always be a valid integer in the range [0-100];
Output
•	Print the exam results for each participant
•	After that, print each language in the format shown above
•	Allowed working time / memory: 100ms / 16MB


____________________________________________________________________________________________
Example_01

Input
Peter-Java-84
George-C#-84
George-C#-70
Katy-C#-94
exam finished

Output
Results:
Peter | 84
George | 84
Katy | 94
Submissions:
Java - 1
C# - 3


____________________________________________________________________________________________
Example_02

Input
Peter-Java-91
George-C#-84
Katy-Java-90
Katy-C#-50
Katy-banned
exam finished

Output
Results:
Peter | 91
George | 84
Submissions:
Java - 2
C# - 2

"""
