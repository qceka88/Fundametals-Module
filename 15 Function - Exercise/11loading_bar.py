def loading_bar(some_number):
    if some_number == 100:
        return '100% Complete!\n[%%%%%%%%%%]'
    return f'{some_number}% [{"%" * (some_number // 10) + "." * (10 - (some_number // 10))}]' \
           f'\nStill loading...'


number = int(input())
result = loading_bar(number)
print(result)



#################################### TASK CONDITION ############################
"""
                       11. * Loading Bar
You will receive a single integer number between 0 and 100 (inclusive)
divisible by 10 without remainder (0, 10, 20, 30...).
Your task is to create a function that returns a loading bar depending 
on the number you have received in the input. Print the result on the console.
or more clarification, see the examples below.


____________________________________________________________________________________________
Example_01

Input
30

Output
30% [%%%.......]
Still loading...


____________________________________________________________________________________________
Example_02

Input
50

Output
50% [%%%%%.....]
Still loading...


____________________________________________________________________________________________
Example_03

Input
100

Output
100% Complete!
[%%%%%%%%%%]

"""
