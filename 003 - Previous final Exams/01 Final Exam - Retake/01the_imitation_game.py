initital_strign = input()

command = input()

while command != 'Decode':
    input_data = command.split('|')
    order = input_data[0]
    if order == 'Move':
        number = int(input_data[1])
        initital_strign = initital_strign[number:] + initital_strign[:number]
    elif order == 'Insert':
        index = int(input_data[1])
        value = input_data[2]
        initital_strign = initital_strign[:index] + value + initital_strign[index:]
    elif order == 'ChangeAll':
        old_letter = input_data[1]
        new_letter = input_data[2]
        initital_strign = initital_strign.replace(old_letter, new_letter)

    command = input()

print(f"The decrypted message is: {initital_strign}")

#################################### TASK CONDITION ############################
"""
                     Problem 1 - The Imitation Game
Problem for exam preparation for the Programming Fundamentals Course @SoftUni.
Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2525#0.

During World War 2, you are a mathematician who has joined the cryptography 
team to decipher the enemy's enigma code. Your job is to create a program to crack the codes. 
On the first line of the input, you will receive the encrypted message. 
After that, until the "Decode" command is given, you will be receiving strings
with instructions for different operations that need to be performed upon the concealed
message to interpret it and reveal its true content. There are several types of instructions, split by '|'
•	"Move {number of letters}":
o	Moves the first n letters to the back of the string
•	"Insert {index} {value}":
o	Inserts the given value before the given index in the string
•	"ChangeAll {substring} {replacement}":
o	Changes all occurrences of the given substring with the replacement text
Input / Constraints
•	On the first line, you will receive a string with a message.
•	On the following lines, you will be receiving commands, split by '|' .
Output
•	After the "Decode" command is received, print this message:
"The decrypted message is: {message}"

____________________________________________________________________________________________
Example_01

Input
zzHe
ChangeAll|z|l
Insert|2|o
Move|3
Decode

Output
The decrypted message is: Hello

Explanation
ChangeAll|z|l
zzHe → llHe (We replace all occurrences of 'z' with 'l')
Insert|2|o
llHe → lloHe (We add an 'o' before the character on index 2)
Move|3
lloHe → Hello (We take the first three characters and move them to the end of the string)
Finally, after receiving the "Decode" command, we print the resulting message.

____________________________________________________________________________________________
Example_02

Input
owyouh
Move|2
Move|3
Insert|3|are
Insert|9|?
Decode	

Output
The decrypted message is: howareyou?

"""