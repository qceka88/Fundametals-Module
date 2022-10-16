############################ variant 01 #########################

def add_lesson(lessons_list, new_title):
    if new_title not in lessons_list:
        lessons_list.append(new_title)
    return lessons_list


def insert_lesson(lessons_list, new_title, lesson_index):
    if new_title not in lessons_list:
        lessons_list.insert(lesson_index, new_title)
    return lessons_list


def remove_lesson(lessons_list, remove_title):
    if remove_title in lessons_list:
        lessons_list.remove(remove_title)
    if f'{remove_title}-Exercise' in lessons_list:
        lessons_list.remove(f'{remove_title}-Exercise')
    return lessons_list


def swap_lesson(lessons_list, first, second):
    if first in lessons_list and second in lessons_list:
        first_index = lessons_list.index(first)
        second_index = lessons_list.index(second)
        lessons_list[first_index], lessons_list[second_index] = lessons_list[second_index], lessons_list[first_index]
        if f'{first}-Exercise' in lessons_list:
            lessons_list.remove(f'{first}-Exercise')
            lessons_list.insert(second_index + 1, f'{first}-Exercise')
        if f'{second}-Exercise' in lessons_list:
            lessons_list.remove(f'{second}-Exercise')
            lessons_list.insert(first_index + 1, f'{second}-Exercise')
    return lessons_list


def add_exercise(lessons_list, lesson_title):
    if lesson_title not in lessons_list:
        lessons_list.append(lesson_title)
    if f'{lesson_title}-Exercise' not in lessons_list:
        index_of_lesson = lessons_list.index(lesson_title)
        lessons_list.insert(index_of_lesson + 1, f'{lesson_title}-Exercise')
    return lessons_list


lessons_schedule = input().split(', ')

while True:
    input_line = input()
    if input_line == 'course start':
        break

    input_data = input_line.split(':')
    command = input_data[0]
    title = input_data[1]

    if command == 'Add':
        lessons_schedule = add_lesson(lessons_schedule, title)
    elif command == 'Insert':
        index = int(input_data[2])
        lessons_schedule = insert_lesson(lessons_schedule, title, index)
    elif command == 'Remove':
        lessons_schedule = remove_lesson(lessons_schedule, title)
    elif command == 'Swap':
        first_lesson = title
        second_lesson = input_data[2]
        lessons_schedule = swap_lesson(lessons_schedule, first_lesson, second_lesson)
    elif command == 'Exercise':
        lessons_schedule = add_exercise(lessons_schedule, title)

for lesson_index, name in enumerate(lessons_schedule):
    print(f"{lesson_index + 1}.{name}")


############################ variant 02 #########################

def swap_order(lessons, current_lesson):
    first_lesson = current_lesson[1]
    second_lesson = current_lesson[2]
    if first_lesson and second_lesson in lessons:
        first_index = int(lessons.index(first_lesson))
        second_index = int(lessons.index(second_lesson))
        lessons[first_index], lessons[second_index] = lessons[second_index], lessons[first_index]
        if f'{first_lesson}-Exercise' in lessons:
            lessons.remove(f'{first_lesson}-Exercise')
            index01 = lessons.index(first_lesson)
            lessons.insert(index01, f'{first_lesson}-Exercise')
        if f'{second_lesson}-Exercise' in lessons:
            lessons.remove(f'{second_lesson}-Exercise')
            index02 = lessons.index(second_lesson) + 1
            lessons.insert(index02, f'{second_lesson}-Exercise')
    return lessons


lessons = input().split(', ')

while True:
    command = input()
    if command == 'course start':
        break

    current_lesson = command.split(':')
    order = current_lesson[0]
    lesson_title = current_lesson[1]

    if order == 'Add' and lesson_title not in lessons:
        lessons.append(lesson_title)
    elif order == 'Insert' and lesson_title not in lessons:
        index = int(current_lesson[2])
        lessons.insert(index, lesson_title)
    elif order == 'Remove':
        lessons.remove(lesson_title)
        if f'{lesson_title}-Exercise' in lessons:
            lessons.remove(f'{lesson_title}-Exercise')
    elif order == 'Swap':
        lessons = swap_order(lessons, current_lesson)
    elif order == 'Exercise':
        if lesson_title in lessons and f'{lesson_title}-Exercise' not in lessons:
            index = lessons.index(lesson_title)
            lessons.insert(index + 1, f'{lesson_title}-Exercise')
        elif lesson_title not in lessons:
            lessons.append(lesson_title)
            lessons.append(f'{lesson_title}-Exercise')

print('\n'.join([f'{i + 1}.{v}' for i, v in enumerate(lessons)]))



#################################### TASK CONDITION ############################
"""
                11.	 *SoftUni Course Planning
Help plan the next Programming Fundamentals course by keeping track of the 
lessons that will be included in the course and all the exercises for the lessons. 
Before the course starts, there are some changes to be made. 
On the first input line, you will receive the initial schedule of lessons 
and exercises that will be part of the next course, separated by a comma and a space ", ". 
Until you receive the "course start" command, you will be given some 
commands to modify the course schedule. 
The possible commands are:
•	"Add:{lessonTitle}" - add the lesson to the end of the schedule if it does not exist.
•	"Insert:{lessonTitle}:{index}" - insert the lesson to the given index, if it does not exist.
•	"Remove:{lessonTitle}" - remove the lesson, if it exists.
•	"Swap:{lessonTitle}:{lessonTitle}" - swap the position of the two lessons if they exist.
•	"Exercise:{lessonTitle}" - add Exercise in the schedule right after the lesson index, 
if the lesson exists and there is no exercise already, in the following 
format "{lessonTitle}-Exercise". If the lesson doesn't exist, add the lesson 
at the end of the course schedule, followed by the Exercise.
Note: Each time you Swap or Remove a lesson, you should do the same with the 
Exercises, if there are any following the lessons.
Input / Constraints
•	On the first line - the initial schedule lessons - strings, separated by comma and space ", ".
•	Until "course start" you will receive commands in the format described above.
Output
•	Print the whole course schedule, each lesson on a new line with its number (index) in the schedule: 
"{lesson index}.{lessonTitle}".
•	Allowed working time / memory: 100ms / 16MB.


____________________________________________________________________________________________
Example_01

Inputt
Data Types, Objects, Lists
Add:Databases
Insert:Arrays:0
Remove:Lists
course start

Output
1.Arrays
2.Data Types
3.Objects
4.Databases

Explanation
We receive the initial schedule. 
Next, we add the Databases lesson, because it doesn't exist. 
We Insert at the given index lesson Arrays because it's not present in the schedule. 
After receiving the last command and removing lesson Lists, we print the whole schedule.


____________________________________________________________________________________________
Example_02

Input
Arrays, Lists, Methods
Swap:Arrays:Methods
Exercise:Databases
Swap:Lists:Databases
Insert:Arrays:0
course start

Output
1.Methods
2.Databases
3.Databases-Exercise
4.Arrays
5.Lists

Explanation
We swap the given lessons because both exist.
After receiving the Exercise command, we see that such a lesson doesn't exist, 
so we add the lesson at the end, followed by the exercise.
We swap Lists and Databases lessons, the
Databases-Exercise is also moved after the Databases lesson.
We skip the next command because we already have such a lesson in our schedule.

"""
