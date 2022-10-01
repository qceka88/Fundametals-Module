sequence_of_numbers = list(map(int, input().split()))

finish_line = len(sequence_of_numbers) // 2
left_car = sequence_of_numbers[:finish_line]
right_car = sequence_of_numbers[len(sequence_of_numbers):finish_line:-1]

left_time = 0
right_time = 0

for time_index in range(finish_line):
    left_racer = left_car[time_index]
    right_racer = right_car[time_index]
    if left_racer == 0:
        left_time *= 0.8
    if right_racer == 0:
        right_time *= 0.8
    left_time += left_racer
    right_time += right_racer

if left_time < right_time:
    print(f"The winner is left with total time: {left_time:.1f}")
else:
    print(f"The winner is right with total time: {right_time:.1f}")

#################################### TASK CONDITION ############################
"""
                   3.	Car Race
Write a program that announces the winner of a car race. 
You will receive a sequence of numbers.
Each number represents the time the car needs to pass through that step (the index). 
There will be two cars. The first one starts from the left side, and the other one 
starts from the right side. The middle index of the sequence is the finish line. 
Calculate the total time each racer needs to reach the finish line and print the winner
with his total time (the racer with less time). If you have a zero in the list,
you should reduce the racer's time that reached it by 20% (from his current time).
The number of elements in the sequence will always be odd.
Print the result in the following format "The winner is {left/right} with total time: {total_time}".
The time should be formatted to the first decimal point.


____________________________________________________________________________________________
Example_01

Input
29 13 9 0 13 0 21 0 14 82 12

Output
The winner is left with total time: 53.8

Explanation
The time of the left racer is (29 + 13 + 9) * 0.8 (because of the zero) + 13 = 53.8.
The time of the right racer is (82 + 12 + 14) * 0.8 + 21 = 107.4.
The winner is the left racer, so we print it.


____________________________________________________________________________________________
Example_02

Input
123 20 4 0 13 0 0 5 5 14 0

Output
The winner is right with total time: 19.2

"""
