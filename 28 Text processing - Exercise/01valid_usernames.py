class Validator:

    def __init__(self, name):
        self.name = name

    def length_of_name_validation(self):
        if 3 <= len(self.name) <= 16:
            return True
        return False

    def symbols_validation(self):
        for symbol in self.name:
            if not (symbol.isalpha() or symbol.isdigit() or symbol == '-' or symbol == '_'):
                return False
        return True

    def redundant_validation(self):
        if ' ' in self.name:
            return False
        return True

    def validated_user(self):
        if self.length_of_name_validation() and self.symbols_validation() and self.redundant_validation():
            return True
        return False


input_data = input().split(', ')

for username in input_data:
    validated = Validator(username)
    if validated.validated_user():
        print(username)





#################################### TASK CONDITION ############################
"""
                                1.	Valid Usernames
Write a program that reads usernames on a single line (separated by ", ") 
and prints all valid usernames on separate lines. 
A valid username:
•	has length between 3 and 16 characters inclusive
•	can contain only letters, numbers, hyphens, and underscores
•	has no redundant symbols before, after, or in between


____________________________________________________________________________________________
Example_01

Input
sh, too_long_username, !lleg@l ch@rs, jeffbutt

Output
jeffbutt


____________________________________________________________________________________________
Example_02

Input
Jeff, john45, ab, cd, peter-ivanov, @smith

Output
Jeff
John45
peter-ivanov

"""
