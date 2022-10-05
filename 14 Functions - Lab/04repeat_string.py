input_string = input()
repeating = int(input())

new_string = lambda x: x * repeating

print(new_string(input_string))



#################################### TASK CONDITION ############################
"""
                     4.	Repeat String
Write a function that receives a string and a counter n. 
The function should return a new string – the result of 
repeating the old string n times. Print the result of the function. Try using lambda.


____________________________________________________________________________________________
Example_01

Input
abc
3	abcabcabc


____________________________________________________________________________________________
Example_02

Input
String
2	StringString

"""
