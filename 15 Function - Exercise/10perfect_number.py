def perfect_number(some_number):
    aliquot_sum = sum([num for num in range(1, (some_number // 2) + 1) if some_number % num == 0])
    if aliquot_sum == some_number:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


number = int(input())

perfection = perfect_number(number)

print(perfection)



#################################### TASK CONDITION ############################
"""
                         10. Perfect Number 
A perfect number is a positive integer that is equal to the sum of its proper
positive divisors. That is the sum of its positive divisors, excluding the
number itself (also known as its aliquot sum).
Write a function that receives an integer number and returns one of the following messages:
•	"We have a perfect number!" - if the number is perfect.
•	"It's not so perfect." - if the number is NOT perfect.
Print the result on the console.


____________________________________________________________________________________________
Example_01

Input
6

Output
We have a perfect number!

Explanation
1 + 2 + 3


____________________________________________________________________________________________
Example_02

Input
28

Output
We have a perfect number!

Explanation
1 + 2 + 4 + 7 + 14


____________________________________________________________________________________________
Example_03

Input
1236498

Output
It's not so perfect.



Hint
Every perfect number is half the sum of all its positive divisors
(including itself) => the sum of all positive divisors
(all of which are divided without remainder) of 6 is 1 + 2 + 3 + 6 = 12.
Half of 12 is 6 => 6 is perfect number.

•You could read more about the perfect number here: https://en.wikipedia.org/wiki/Perfect_number

"""
