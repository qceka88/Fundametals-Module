import re


class Extracting:

    def __init__(self, string):
        self.string = string

    def regex_action(self):
        matched_name = re.findall(r'(\b\_)([A-Za-z0-9]+)\b', self.string)
        return matched_name

    def __repr__(self):
        return ','.join(name[1] for name in self.regex_action())


input_line = input()

output = Extracting(input_line)
print(output)



#################################### TASK CONDITION ############################
"""
                     2.	Find Variable Names in Sentences
Write a program that finds all variable names in each string.
A variable name starts with an underscore ("_") and contains only capital and 
non-capital letters and digits. Extract only their names without the underscore. 
Try to do this only with regular expressions.
The output consists of all variable names extracted and printed on a single line,
separated by a comma.

____________________________________________________________________________________________
Example_01

Input
The _id and _age variables are both integers.

Output
id,age


____________________________________________________________________________________________
Example_02

Input
Calculate the _area of the _perfectRectangle object.

Output
area,perfectRectangle

____________________________________________________________________________________________
Example_03

Input
__invalidVariable _evenMoreInvalidVariable_ _validVariable	

Output
validVariable

"""
