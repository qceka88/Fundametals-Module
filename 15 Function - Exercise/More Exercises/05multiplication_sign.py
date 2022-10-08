def multiplication_sign(first, second, third):
    numbers_list = [first, second, third]
    check = [num for num in numbers_list if num < 0]
    if 0 in numbers_list:
        return 'zero'
    elif len(check) % 2 == 0:
        return 'positive'
    else:
        return 'negative'


first_number = int(input())
second_number = int(input())
third_number = int(input())

result = multiplication_sign(first_number, second_number, third_number)

print(result)




#################################### TASK CONDITION ############################
"""
                           5.	Multiplication Sign
You will receive three integer numbers.
Write a program that finds if their multiplication (the result) is negative, 
positive, or zero. Try to do this WITHOUT multiplying the 3 numbers.


____________________________________________________________________________________________
Example_01

Input
2
3
-1

Output
negative


____________________________________________________________________________________________
Example_02

Input
2
3
1

Output
positive

"""
