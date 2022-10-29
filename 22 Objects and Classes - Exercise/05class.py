class Class:
    __students_count = 22

    def __init__(self, name):
        self.name = name
        self.students = []
        self.grades = []

    def add_student(self, name: str, grade: float):
        if len(self.students) < Class.__students_count:
            self.students.append(name)
            self.grades.append(grade)

    def get_average_grade(self):
        average_grade = sum(self.grades) / len(self.students)
        return average_grade

    def __repr__(self):
        students = ', '.join(self.students)
        average_grade = Class.get_average_grade(self)
        return f"The students in {self.name}: {students}. Average grade: {average_grade:.2f}"


# Part below is test code from example


a_class = Class("11B")
a_class.add_student("Peter", 4.80)
a_class.add_student("George", 6.00)
a_class.add_student("Amy", 3.50)
print(a_class)

#################################### TASK CONDITION ############################
'''
                            5.	Class
Create a class Class. The __init__ method should receive the name of the class. 
Each class should also have 2 empty lists - students and grades. 
Create a class attribute __students_count equal to 22. 
The class should also have 3 additional methods:
•	add_student(name: str, grade: float) - adds the student and the 
grade in the two lists if there is free space in the class
•	get_average_grade() - returns the average of all existing grades formatted 
to the second decimal point (as a number)
•	__repr__ - returns the string (single line):
"The students in {class_name}: {students}. Average grade: {average_grade}". 
The students must be separated by a comma and a space: ", ".

_______________________________________________
Example

Test Code	(no input data in this task)

a_class = Class("11B")
a_class.add_student("Peter", 4.80)
a_class.add_student("George", 6.00)
a_class.add_student("Amy", 3.50)
print(a_class)

Output
The students in 11B: Peter, George, Amy. Average grade: 4.77

'''
