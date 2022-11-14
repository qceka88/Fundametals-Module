import re


class Regex:

    def __init__(self, data):
        self.data = data

    def regex_action(self):
        pattern = r'(^|(?<=\s))-?(\d*)(\.\d+)?($|(?=\s))'
        match = re.finditer(pattern, input_data)
        return match


class Numbers:

    def __init__(self, some_data):
        self.some_data = some_data

    def extracting(self):
        extracted_data = Regex(self.some_data)
        return extracted_data.regex_action()

    def printing(self):
        for matched_number in self.extracting():
            print(matched_number.group(), end=' ')


input_data = input()

output = Numbers(input_data)
output.printing()


#################################### TASK CONDITION ############################
"""
                         4.	Match Numbers
Write a program that finds all integer and floating-point numbers in a string.
Compose the Regular Expression
A number has the following characteristics:
•	Has either whitespace before it or the start of the string (match either ^ or what's called a positive lookbehind).
The entire syntax for the beginning of your RegEx might look something like "(^|(?<=\s))".
•	The number might or might not be negative, so it might have a hyphen on its left side ("-").
•	It consists of one or more digits.
•	Might or might not have digits after the decimal point
•	The decimal part (if it exists) consists of a period (".") and one or more digits after it. Use a capturing group.
•	Has either whitespace before it or the end of the string (match either $ or what's called a positive lookahead).
The syntax for the end of the RegEx might look something like "($|(?=\s))".

You can follow the table below to help with composing your RegEx:
Match ALL of these
1 -1 123 -123 123.456 -123.456


Match NONE of these
1s s2 s-s -1- _55_ s-2 s-3.5 s-1.1 00.5

Find all the numbers from the string and print them on the console, separated by spaces.

____________________________________________________________________________________________
Example

Input
1 -1 1s 123 s-s -123 _55_ _f 123.456 -123.456 s-1.1 s2 -1- zs-2 s-3.5 00.5

Output 
1 -1 123 -123 123.456 -123.456

"""
