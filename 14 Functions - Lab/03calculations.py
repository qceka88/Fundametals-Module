def calculation(number01, number02, order):
    result = 0
    if order == "multiply":
        result = number01 * number02
    elif order == "divide":
        result = number01 / number02
    elif order == "add":
        result = number01 + number02
    elif order == "subtract":
        result = number01 - number02
    return int(result)


action = input()
first_number = int(input())
second_number = int(input())

print(calculation(first_number, second_number, action))



#################################### TASK CONDITION ############################
"""
3.	Calculations
Create a function that receives three parameters,
calculates a result depending on the given operator, and returns it.
Print the result of the function.
The input comes as three parameters – an operator as a string and two integer numbers. 
The operator can be one of the following:  "multiply", "divide", "add", "subtract". 


____________________________________________________________________________________________
Example_01

Input
subtract
5
4

Output
1


____________________________________________________________________________________________
Example_02

Input
divide
8
4

Output
2

"""
