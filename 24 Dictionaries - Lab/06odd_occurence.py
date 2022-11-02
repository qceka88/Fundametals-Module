from collections import defaultdict

line = input().split()
collect = defaultdict(int)

for element in line:
    collect[element.lower()] += 1

print(' '.join(key for key, value in collect.items() if value % 2 != 0))



#################################### TASK CONDITION ############################
"""
                      6.	Odd Occurrences
Write a program that prints all elements from a given sequence 
of words that occur an odd number of times (case-insensitive) in it.
•	Words are given on a single line, space-separated.
•	Print the result elements in lowercase, in their order of appearance.

____________________________________________________________________________________________
Example_01

Input
Java C# PHP PHP JAVA C java

Output
java c# c

____________________________________________________________________________________________
Example_02

Input
3 5 5 hi pi HO Hi 5 ho 3 hi pi

Output
5 hi

____________________________________________________________________________________________
Example_03

Input
a a A SQL xx a xx a A a XX c

Output
a sql xx c


"""
