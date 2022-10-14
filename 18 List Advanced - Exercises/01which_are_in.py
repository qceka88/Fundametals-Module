substrings = input().split(', ')
words = input().split(', ')

occurrences = []

for substring in substrings:
    for word in words:
        if substring in word and substring not in occurrences:
            occurrences.append(substring)

print(occurrences)



#################################### TASK CONDITION ############################
"""
                          1.	Which Are In?
You will be given two sequences of strings, separated by ", ". 
Print a new list containing only the strings from the first input line, 
which are substrings of any string in the second input line.


____________________________________________________________________________________________
Example_01

Input
arp, live, strong
lively, alive, harp, sharp, armstrong

Output
['arp', 'live', 'strong']

____________________________________________________________________________________________
Example_02

Input

tarp, mice, bull
lively, alive, harp, sharp, armstrong	[]

"""
