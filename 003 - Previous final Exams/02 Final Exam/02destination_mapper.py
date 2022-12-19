import re

initial_string = input()
pattern = r'(?P<sep>=|/)([A-Z]{1}[A-z]{2,})(?P=sep)'
match = re.findall(pattern, initial_string)

destinations_list = []
points = 0

for destination in match:
    destinations_list.append(destination[1])
    points += len(destination[1])

print(f"Destinations: {', '.join(destinations_list)}")
print(f"Travel Points: {points}")

#################################### TASK CONDITION ############################
"""
                                    Problem 2 - Destination Mapper
Problem for exam preparation for the Programming Fundamentals Course @SoftUni.
Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2518#1.

Now that you have planned out your tour, you are ready to go! 
Your next task is to mark all the points on the map that you are going to visit.
You will be given a string representing some places on the map. 
You have to filter only the valid ones. A valid location is:
•	Surrounded by "=" or "/" on both sides (the first and the last symbols must match)
•	After the first "=" or "/" there should be only letters 
(the first must be upper-case, other letters could be upper or lower-case)
•	The letters must be at least 3
Example: In the string "=Hawai=/Cyprus/=Invalid/invalid==i5valid=/I5valid/=i=" 
only the first two locations are valid.
After you have matched all the valid locations, you have to calculate travel points. 
They are calculated by summing the lengths of all the valid destinations that you have found on the map. 
In the end, on the first line, print: "Destinations: {destinations joined by ', '}". 
On the second line, print "Travel Points: {travel_points}".
Input / Constraints
•	You will receive a string representing the locations on the map
•	JavaScript: you will receive a single parameter: string
Output
•	Print the messages described above

____________________________________________________________________________________________
Example_01

Input
=Hawai=/Cyprus/=Invalid/invalid==i5valid=/I5valid/=i=


Output
Destinations: Hawai, Cyprus
Travel Points: 11

____________________________________________________________________________________________
Example_02

Input
ThisIs some InvalidInput

Output
Destinations:
Travel Points: 0

"""