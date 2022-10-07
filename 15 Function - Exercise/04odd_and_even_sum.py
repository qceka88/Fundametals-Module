def odd_sum(num):
    odd_number = sum([int(odd) for odd in num if int(odd) % 2 != 0])
    return odd_number


def even_sum(num):
    even_number = sum([int(even) for even in num if int(even) % 2 == 0])
    return even_number

number = input()

sum_of_odd_digits = odd_sum(number)
sum_of_even_digits = even_sum(number)

print(f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}")



#################################### TASK CONDITION ############################
"""
                            4. Odd and Even Sum
You will receive a single number. You should write a function that
returns the sum of all even and all odd digits in a given number.
The result should be returned as a single string in the format: 
"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}"
Print the result of the function on the console.


____________________________________________________________________________________________
Example_01

Input
1000435

Output
Odd sum = 9, Even sum = 4


____________________________________________________________________________________________
Example_02

Input
3495892137259234

Output
Odd sum = 54, Even sum = 22

"""
