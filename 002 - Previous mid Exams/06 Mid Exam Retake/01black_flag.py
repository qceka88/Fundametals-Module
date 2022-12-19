days = int(input())
daily_plunder = int(input())
expected_plunder = int(input())

gained_plunder = 0

for day in range(1, days + 1):
    if day % 3 == 0:
        gained_plunder += daily_plunder * 1.5
    else:
        gained_plunder += daily_plunder
    if day % 5 == 0:
        gained_plunder *= 0.7

if gained_plunder >= expected_plunder:
    print(f"Ahoy! {gained_plunder:.2f} plunder gained.")
else:
    percentage = gained_plunder / expected_plunder * 100
    print(f"Collected only {percentage:.2f}% of the plunder.")



#################################### TASK CONDITION ############################
"""
                   Problem 1 - Black Flag 
Problem for exam preparation for the Programming Fundamentals Course @SoftUni.
Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/1773#0.

Pirates are invading the sea, and you're tasked to help them plunder
Create a program that checks if target plunder is reached. 
First, you will receive how many days the pirating lasts.
 Then you will receive how much the pirates plunder for a day. 
 Last you will receive the expected plunder at the end.
Calculate how much plunder the pirates manage to gather. Each day they gather the plunder. 
Keep in mind that they attack more ships every third day and 
add additional plunder to their total gain, which is 50% of the daily plunder.
 Every fifth day the pirates encounter a warship, and after the battle, they lose 30% of their total plunder.
If the gained plunder is more or equal to the target, print the following:
"Ahoy! {totalPlunder} plunder gained."
If the gained plunder is less than the target. Calculate the percentage left and print the following:
"Collected only {percentage}% of the plunder."
Both numbers should be formatted to the 2nd decimal place.
Input
•	On the 1st line, you will receive the days of the plunder – an integer number in the range [0…100000]
•	On the 2nd line, you will receive the daily plunder – an integer number in the range [0…50]
•	On the 3rd line, you will receive the expected plunder – a real number in the range [0.0…10000.0]
Output
•	 In the end, print whether the plunder was successful or not, following the format described above.


____________________________________________________________________________________________
Example_01



Input
5
40
100	

Output
Ahoy! 154.00 plunder gained.


Explanation
The days are 5, and the daily plunder is 40.
On the third day, the total plunder is 120,
and since it is a third day, they gain an 
additional 50% from the daily plunder, which adds up to 140.
On the fifth day, the plunder is 220, but they battle with a warship 
and lose 30% of the collected cargo, and the total becomes 154. That is more than expected..

____________________________________________________________________________________________
Example_02


Input

10
20
380

Output
Collected only 36.29% of the plunder.

"""
