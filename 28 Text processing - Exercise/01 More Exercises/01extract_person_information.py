class Extract:

    def __init__(self, text):
        self.text = text

    def find_name(self, some_text):
        start = some_text.index('@')
        end = some_text.index('|')
        name = some_text[start + 1:end]
        return name

    def find_age(self, some_text):
        start = some_text.index('#')
        end = some_text.index('*')
        age = some_text[start + 1:end]
        return age

    def checking_the_text(self):
        person_name = self.find_name(self.text)
        person_age = self.find_age(self.text)
        return f'{person_name} is {person_age} years old.'

    def __repr__(self):
        return self.checking_the_text()


number_of_lines = int(input())

for string in range(number_of_lines):
    current_string = input()
    extracting = Extract(current_string)
    print(extracting)

#################################### TASK CONDITION ############################
"""
                            1.	Extract Person Information
Write a program that reads N lines of strings and extracts the name and the age of a given person:
•	The person's name will be surrounded by "@" and "|" in the format "@{name}|".
•	The person's age will be surrounded by "#" and "*" in the format "#{age}*".
Example: "Hello my name is @Peter| and I am #20* years old." 
For each found name-age pair, print a line in the following format "{name} is {age} years old."


____________________________________________________________________________________________
Example_01

Input
2
Here is a name @George| and an age #18*
Another name @Billy| #35* is his age

Output
George is 18 years old.
Billy is 35 years old.


____________________________________________________________________________________________
Example_02

Input
3
random name @lilly| random digits #5*age
@Marry| with age #19*
here Comes @Garry|he is #48* years old

Output
lilly is 5 years old.
Marry is 19 years old.
Garry is 48 years old.

"""
