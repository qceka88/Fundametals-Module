def palindrome(numbers):
    palindrom = numbers == numbers[::-1]
    return palindrom


list_of_numbers = list(map(int, input().split(', ')))

for number in list_of_numbers:
    result = palindrome(str(number))
    print(result)



#################################### TASK CONDITION ############################
"""
                     8. Palindrome Integers
A palindrome is a number that reads the same backward as forward,
such as 323 or 1001. Write a function that receives a list of positive integers,
separated by comma and space ", ".
The function should check if each integer is a palindrome - True or False. Print the result.


____________________________________________________________________________________________
Example_01

Input
123, 323, 421, 121

Output
False
True
False
True


____________________________________________________________________________________________
Example_02

Input
32, 2, 232, 1010

Output
False
True
True
False

"""
