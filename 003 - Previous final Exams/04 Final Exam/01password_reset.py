password = input()

while True:
    command = input()
    if command == 'Done':
        print(f"Your password is: {password}")
        break
    input_data = command.split()
    action = input_data[0]

    if action == 'TakeOdd':
        password = ''.join([symbol for index, symbol in enumerate(password) if index % 2 != 0])
        print(password)
    elif action == 'Cut':
        index = int(input_data[1])
        lenght = int(input_data[2])
        password = password[:index] + password[index + lenght:]
        print(password)
    elif action == 'Substitute':
        substring = input_data[1]
        if substring not in password:
            print('Nothing to replace!')
        else:
            substitute = input_data[2]
            password = password.replace(substring, substitute)
            print(password)

#################################### TASK CONDITION ############################
"""
Problem 1 - Password Reset
Problem for exam preparation for the Programming Fundamentals Course @SoftUni.
Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2303#0.

Yet again, you have forgotten your password. Naturally, 
it's not the first time this has happened. Actually, you got so 
tired of it that you decided to help yourself with an intelligent solution.
Write a password reset program that performs a series of 
commands upon a predefined string. First, you will receive a string, 
and afterward, until the command "Done" is given, you will be receiving 
strings with commands split by a single space. The commands will be the following:
•	"TakeOdd"
o	 Takes only the characters at odd indices and concatenates them to 
obtain the new raw password and then prints it.
•	"Cut {index} {length}"
o	Gets the substring with the given length starting from the given 
index from the password and removes its first occurrence, 
then prints the password on the console.
o	The given index and the length will always be valid.
•	"Substitute {substring} {substitute}"
o	If the raw password contains the given substring, replaces all of its 
occurrences with the substitute text given and prints the result.
o	If it doesn't, prints "Nothing to replace!".
Input
•	You will be receiving strings until the "Done" command is given.
Output
•	After the "Done" command is received, print:
o	"Your password is: {password}"
Constraints
•	The indexes from the "Cut {index} {length}" command will always be valid.

____________________________________________________________________________________________
Example_01

Input
Siiceercaroetavm!:?:ahsott.:i:nstupmomceqr 
TakeOdd
Cut 15 3
Substitute :: -
Substitute | ^
Done

Output
icecream::hot::summer
icecream::hot::mer
icecream-hot-mer
Nothing to replace!
Your password is: icecream-hot-mer

Explanation
TakeOdd -> We only take the chars at odd indices 1, 3, 5 etc.
Siiceercaroetavm!:?:ahsott.:i:nstupmomceqr -> icecream::hot::summer
Cut 15  3 -> We cut a substring starting at 
index 15 with length 3, then remove it from the raw password:
icecream::hot::summer -> sum
Substitute :: - -> We replace "::" with "-":
icecream::hot::summer -> icream-hot-summer
Substitute | ^ -> "|" is not found anywhere in 
the raw password, so we print "Nothing to replace!"
Finally, after receiving the "Done" command, we 
print the resulting password in the proper format.

____________________________________________________________________________________________
Example_02

Input
up8rgoyg3r1atmlmpiunagt!-irs7!1fgulnnnqy
TakeOdd
Cut 18 2
Substitute ! ***
Substitute ? .!.
Done

Output
programming!is!funny
programming!is!fun
programming***is***fun
Nothing to replace!
Your password is: programming***is***fun

"""