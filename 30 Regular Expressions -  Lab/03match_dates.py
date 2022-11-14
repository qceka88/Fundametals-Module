import re


class Regex:

    def __init__(self, some_data):
        self.some_data = some_data

    def regex_action(self):
        match = re.findall(r'\b(\d{2})(?P<sep>/|\.|-)([A-Z]{1}[a-z]{2})(?P=sep)(\d{4})', self.some_data)
        return match


class Dates:

    def __init__(self, data):
        self.data = data

    def extracting(self):
        extracted_data = Regex(self.data)
        return extracted_data.regex_action()

    def printing(self):
        for date in self.extracting():
            print(f'Day: {date[0]}, Month: {date[2]}, Year: {date[3]}')


input_data = input()

output = Dates(input_data)
output.printing()

#################################### TASK CONDITION ############################
"""
                             3.	Match Dates
Write a program, which matches a date in the format "dd{separator}MMM{separator}yyyy".
 Use capturing groups in your regular expression.
Compose the Regular Expression
Every valid date has the following characteristics:
•	It always starts with two digits, followed by a separator
•	After that, it has one uppercase and two lowercase letters (e.g., Jan, Mar).
•	After that, it has a separator and exactly 4 digits (for the year).
•	The separator could be one of these symbols: a period ("."), 
a hyphen ("-") or a forward-slash ("/").
•	The separator must be the same for the whole date (e.g., 13.03.2016 is valid, 13.03/2016 is NOT). 
Use a group backreference to check for this.

Now it is time to find all the valid dates in the input and print each
date in the following format: "Day: {day}, Month: {month}, Year: {year}", each on a new line.

Match ALL of these
13/Jul/1928, 10-Nov-1934, 25.Dec.1937

Match NONE of these
01/Jan-1951, 23/sept/1973, 1/Feb/2016


____________________________________________________________________________________________
Example


Input
13/Jul/1928, 10-Nov-1934, , 01/Jan-1951,f 25.Dec.1937 23/09/1973, 1/Feb/2016

Output
Day: 13, Month: Jul, Year: 1928
Day: 10, Month: Nov, Year: 1934
Day: 25, Month: Dec, Year: 1937


"""
