number_of_students = int(input())
academy = {}
for student in range(number_of_students):
    name = input()
    grade = float(input())
    if name not in academy.keys():
        academy[name] = []
    academy[name].append(grade)

for student_name, grades in academy.items():
    average_grade = sum(grades) / len(grades)
    if average_grade >= 4.50:
        print(f"{student_name} -> {average_grade:.2f}")




#################################### TASK CONDITION ############################
"""
                          9.	 Student Academy
Write a program that keeps the information about students and their grades. 
On the first line, you will receive an integer number representing the 
next pair of rows. On the next lines, you will be receiving each student's name and their grade. 
Keep track of all grades for each student and keep only the students with an 
average grade higher than or equal to 4.50. Print the final dictionary with students 
and their average grade in the following format:
"{name} -> {averageGrade}"
Format the average grade to the 2nd decimal place.


____________________________________________________________________________________________
Example_01

Input
5
John
5.5
John
4.5
Alice
6
Alice
3
George
5

Output
John -> 5.00
Alice -> 4.50
George -> 5.00


____________________________________________________________________________________________
Example_02

Input
5
Amanda
3.5
Amanda
4
Rob
5.5
Christian
5
Robert
6

Output
Rob -> 5.50
Christian -> 5.00
Robert -> 6.00

"""
