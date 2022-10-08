def password_check(some_string):
    valid_password = True
    if len(some_string) < 6 or len(some_string) > 10:
        valid_password = False
        print("Password must be between 6 and 10 characters")
    if not some_string.isalnum():
        valid_password = False
        print("Password must consist only of letters and digits")
    digit_count = [digit for digit in some_string if digit.isdigit()]
    if len(digit_count) < 2:
        valid_password = False
        print("Password must have at least 2 digits")
    return valid_password


password = input()

result = password_check(password)

if result:
    print('Password is valid')

#################################### TASK CONDITION ############################
"""
9. Password Validator
Write a function that checks if a given password is valid. Password validations are:
•	It should be 6 - 10 (inclusive) characters long
•	It should consist only of letters and digits
•	It should have at least 2 digits 
If a password is valid, print "Password is valid".
Otherwise, for every unfulfilled rule, print a message:
•	"Password must be between 6 and 10 characters"
•	"Password must consist only of letters and digits"
•	"Password must have at least 2 digits"


____________________________________________________________________________________________
Example_01

Input
logIn

Output
Password must be between 6 and 10 characters
Password must have at least 2 digits


____________________________________________________________________________________________
Example_02

Input
MyPass123

Output
Password is valid


____________________________________________________________________________________________
Example_03

Input
Pa$s$s

Output
Password must consist only of letters and digits
Password must have at least 2 digits

"""
