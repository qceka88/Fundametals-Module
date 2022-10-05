def grades(number: float):
    if 2 <= number <= 2.99:
        return 'Fail'
    elif 3 <= number <= 3.49:
        return 'Poor'
    elif 3.50 <= number <= 4.49:
        return 'Good'
    elif 4.50 <= number <= 5.49:
        return 'Very Good'
    elif 5.50 <= number <= 6.00:
        return 'Excellent'


input_grade = float(input())

print(grades(input_grade))



#################################### TASK CONDITION ############################
"""
                           2.	Grades
Write a function that receives a grade between 2.00 and 6.00 and prints 
the corresponding grade in words.
•	2.00 – 2.99 - "Fail"
•	3.00 – 3.49 - "Poor"
•	3.50 – 4.49 - "Good"
•	4.50 – 5.49 - "Very Good"
•	5.50 – 6.00 - "Excellent"


____________________________________________________________________________________________
Example_01

Input
3.33

Output
Poor


____________________________________________________________________________________________
Example_02

Input
4.50

Output
Very Good


____________________________________________________________________________________________
Example_03

Input
2.99

Output
Fail

"""
