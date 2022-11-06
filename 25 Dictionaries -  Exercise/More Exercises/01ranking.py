def validation(students_dict, contest, secret_word, user, contest_score, dict_contest):
    valid = False
    if contest in dict_contest and secret_word == dict_contest[contest]:
        valid = True
    if valid:
        if user not in students_dict:
            students_dict[user] = {}
        if contest not in students_dict[user]:
            students_dict[user][contest] = 0
        if students_dict[user][contest] < int(contest_score):
            students_dict[user][contest] = int(contest_score)
    return students_dict


def calculating(students_registered):
    name_best = ''
    points_best = 0
    for user in students_registered.keys():
        current_points = sum(students_registered[user].values())
        if current_points > points_best:
            name_best = user
            points_best = current_points
    return name_best, points_best


contest_dict = {}
registered_students = {}

while True:
    command = input()
    if command == 'end of contests':
        break
    contest_name, password = command.split(':')
    contest_dict[contest_name] = password

while True:
    input_line = input()
    if input_line == 'end of submissions':
        break
    course, password, username, points = input_line.split('=>')
    registered_students = validation(registered_students, course, password, username, points, contest_dict)

best_candidate, best_points = calculating(registered_students)

print(f"Best candidate is {best_candidate} with total {best_points} points.")
print('Ranking:')
for name_of_student, tasks in sorted(registered_students.items()):
    print(name_of_student)
    for course_name, score in sorted(tasks.items(), key=lambda v: -v[1]):
        print(f'#  {course_name} -> {score}')




#################################### TASK CONDITION ############################
"""
                                 1.	Ranking
Here comes the final and the most interesting part – the Final ranking 
of the candidate-interns. The final ranking is determined by the points of 
the interview tasks and by the points from the exams in SoftUni. Here is your 
final task. You will receive some lines of input in the format 
"{contest}:{password for contest}" until you receive "end of contests". 
Save that data because you will need it later. After that you will receive other 
type of inputs in format "{contest}=>{password}=>{username}=>{points}" until you 
receive "end of submissions". Here is what you need to do.
•	Check if the contest is valid (It is considered valid if you received it in the first type of input)
•	Check if the password is correct for the given contest
•	If the contest and the password is valid, save the user with the contest 
they take part in (a user can take part in many contests) and the points the 
user has in the given contest. If you receive the same contest and the same user 
update the points only if the new ones are more than the older ones.
In the end, you should print the info for the user with the most points 
(total points for all contents they participated in) in the format "Best candidate is 
{user} with total {total_points} points.". After that print all students ordered by 
their names. For each user print each contest with the points in descending order. 
See the examples.
Input
•	Strings in format "{contest}:{password for contest}" until the "end of contests" command. 
There will be no case with two equal contests
•	Strings in format "{contest}=>{password}=>{username}=>{points}" 
until the "end of submissions" command.
•	There will be no case with 2 or more users with same total points!
Output
•	On the first line, print the best user in format "Best candidate 
is {user} with total {total points} points.".
•	Then print all students ordered as mentioned above in format:
"{user_name1}
#  {contest1} -> {points}
#  {contest2} -> {points} 
…
#  {contestN} -> {points}"
Constraints
•	The strings may contain any ASCII character except from (:, =, >).
•	The numbers will be in range [0 - 10000].
•	Second input is always valid.


____________________________________________________________________________________________
Example_01

Input
Part One Interview:success
JS Fundamentals:fundExam
C# Fundamentals:fundPass
Algorithms:fun
end of contests
C# Fundamentals=>fundPass=>Tanya=>350
Algorithms=>fun=>Tanya=>380
Part One Interview=>success=>Nikola=>120
Java Basics Exam=>wrong_pass=>Teo=>400
Part One Interview=>success=>Tanya=>220
OOP Advanced=>password123=>Kay=>231
C# Fundamentals=>fundPass=>Tanya=>250
C# Fundamentals=>fundPass=>Nikola=>200
JS Fundamentals=>fundExam=>Tanya=>400
end of submissions

Output
Best candidate is Tanya with total 1350 points.
Ranking:
Nikola
#  C# Fundamentals -> 200
#  Part One Interview -> 120
Tanya
#  JS Fundamentals -> 400
#  Algorithms -> 380
#  C# Fundamentals -> 350
#  Part One Interview -> 220


____________________________________________________________________________________________
Example_02

Input
Java Advanced:funpass
Part Two Interview:success
Math Concept:asdasd
Java Web Basics:forrF
end of contests
Math Concept=>ispass=>Monika=>290
Java Advanced=>funpass=>Simona=>400
Part Two Interview=>success=>Drago=>120
Java Advanced=>funpass=>Petyr=>90
Java Web Basics=>forrF=>Simona=>280
Part Two Interview=>success=>Petyr=>0
Math Concept=>asdasd=>Drago=>250
Part Two Interview=>success=>Simona=>200
end of submissions

Output
Best candidate is Simona with total 880 points.
Ranking:
Drago
#  Math Concept -> 250
#  Part Two Interview -> 120
Petyr
#  Java Advanced -> 90
#  Part Two Interview -> 0
Simona
#  Java Advanced -> 400
#  Java Web Basics -> 280
#  Part Two Interview -> 200

"""
