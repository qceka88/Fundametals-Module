employes = list(map(int, input().split()))
happy_factor = int(input())
increase_happy = [person * happy_factor for person in employes]
happy_employee = [happy for happy in increase_happy if happy > (sum(increase_happy) / len(increase_happy))]

if len(happy_employee) >= len(employes) // 2:
    print(f"Score: {len(happy_employee)}/{len(employes)}. Employees are happy!")
else:
    print(f"Score: {len(happy_employee)}/{len(employes)}. Employees are not happy!")



#################################### TASK CONDITION ############################
"""
7.	The Office
You will receive two lines of input: 
•	a list of employees' happiness as a string of numbers separated by a single space 
•	a happiness improvement factor (single number).
Your task is to find out if the employees are generally happy in their office. 
First, multiply each employee's happiness by the factor.
Then, print one of the following lines:
•	If half or more of the employees have happiness greater than or equal to the average:
"Score: {happy_count}/{total_count}. Employees are happy!"
•	Otherwise:
"Score: {happy_count}/{total_count}. Employees are not happy!"


____________________________________________________________________________________________
Example_01

Input
1 2 3 4 2 1
3

Output
Score: 2/6. Employees are not happy!

Explanation
After the mapping:
3 6 9 12 6 3
After the filtration:
9 12
2/6 people are happy, so the overall happiness is bad


____________________________________________________________________________________________
Example_02

Input
2 3 2 1 3 3
4

Output
Score: 3/6. Employees are happy!

Explanation
Half of the people are happy, so the overall happiness is good

"""
