##################################### variant 01 #####################################
import re

input_string = input()
pattern = r'(\=|\/)([A-Z][A-Za-z]{2,})\1'
match = re.findall(pattern, input_string)
travel_points = sum([len(points[1]) for points in match])
print(f"Destinations: {', '.join(destination[1] for destination in match)}")
print(f"Travel Points: {travel_points}")

destinations = ', '.join([destination[1] for destination in match])

##################################### variant 02 #####################################

import re


class Regex:

    def __init__(self, some_pattern, some_string):
        self.some_pattern = some_pattern
        self.some_string = some_string

    def regex_action(self):
        match = re.findall(self.some_pattern, self.some_string)
        return match


class Extractor:
    __magic = r'(\=|\/)([A-Z][A-Za-z]{2,})\1'

    def __init__(self, input_data):
        self.input_data = input_data

    def separate_data(self):
        data = Regex(Extractor.__magic, self.input_data).regex_action()
        travel_points = sum([len(points[1]) for points in data])
        destinations = ', '.join(destination[1] for destination in data)
        return destinations, travel_points

    def __repr__(self):
        destiantion, points = self.separate_data()
        return f"Destinations: {destiantion}\nTravel Points: {points}"


input_string = input()
result = Extractor(input_string)
print(result)


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