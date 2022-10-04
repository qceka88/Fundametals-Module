numbers = int(input())

positive_numbers = []
negative_numbers = []

for number in range(numbers):
    current_number = int(input())
    if current_number < 0:
        negative_numbers.append(current_number)
    else:
        positive_numbers.append(current_number)

count_positives = len(positive_numbers)
sum_of_negatives = sum(negative_numbers)

print(positive_numbers)
print(negative_numbers)
print(f"Count of positives: {count_positives}")
print(f"Sum of negatives: {sum_of_negatives}")




#################################### TASK CONDITION ############################
"""

                                 3.	List Statistics
On the first line, you will receive a number n. 
On the following n lines, you will receive integers. 
You should create and print two lists:
•	One with all the positives (including 0) numbers
•	One with all the negatives numbers
Finally, print the following message: 
"Count of positives: {count_positives}
Sum of negatives: {sum_of_negatives}"


____________________________________________________________________________________________
Example_01

Input
10
3
2
-15
-4

Output
[10, 3, 2]
[-15, -4]
Count of positives: 3
Sum of negatives: -19


____________________________________________________________________________________________
Example_02

Input
6
11
2
35
599
31
20

Output
[11, 2, 35, 599, 31, 20]
[]
Count of positives: 6
Sum of negatives: 0

"""