activation_key = input()

while True:
    input_data = input()
    if input_data == 'Generate':
        print(f"Your activation key is: {activation_key}")
        break
    command = input_data.split('>>>')
    order = command[0]
    substring = command[1]

    if order == 'Contains':
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print("Substring not found!")
    elif order == 'Flip':
        sub_command = substring
        start_index = int(command[2])
        end_index = int(command[3])
        if sub_command == 'Upper':
            uppered_part = (activation_key[start_index:end_index]).upper()
            activation_key = activation_key[:start_index] + uppered_part + activation_key[end_index:]
        elif sub_command == 'Lower':
            lowered_part = (activation_key[start_index:end_index]).lower()
            activation_key = activation_key[:start_index] + lowered_part + activation_key[end_index:]
        print(activation_key)
    elif order == 'Slice':
        start_index = int(substring)
        end_index = int(command[2])
        activation_key = activation_key[:start_index] + activation_key[end_index:]
        print(activation_key)

#################################### TASK CONDITION ############################
"""
                   Problem 1 - Activation Keys
Problem for exam preparation for the Programming Fundamentals Course @SoftUni.
Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2302#0.

You are about to make some good money, but first, you need to think of a way to 
verify who paid for your product and who didn't. You have decided to let 
people use the software for a free trial period and then require an activation 
key to continue using the product. Before you can cash out, the last step is to 
design a program that creates unique activation keys for each user. So, waste no more time and start typing!
The first line of the input will be your raw activation key. It will consist of letters and numbers only. 
After that, until the "Generate" command is given, you will be receiving strings 
with instructions for different operations that need to be performed upon the raw activation key.
There are several types of instructions, split by ">>>":
•	"Contains>>>{substring}":
o	If the raw activation key contains the given substring, prints: "{raw activation key} contains {substring}".
o	Otherwise, prints: "Substring not found!"
•	"Flip>>>Upper/Lower>>>{startIndex}>>>{endIndex}":
o	Changes the substring between the given indices (the end index is exclusive) 
to upper or lower case and then prints the activation key.
o	All given indexes will be valid.
•	"Slice>>>{startIndex}>>>{endIndex}":
o	Deletes the characters between the start and end indices (the end index is exclusive) and prints the activation key.
o	Both indices will be valid.
Input
•	The first line of the input will be a string consisting of letters and numbers only. 
•	After the first line, until the "Generate" command is given, you will be receiving strings.
Output
•	After the "Generate" command is received, print:
o	"Your activation key is: {activation key}"
____________________________________________________________________________________________
Example_01

Input 
abcdefghijklmnopqrstuvwxyz
Slice>>>2>>>6
Flip>>>Upper>>>3>>>14
Flip>>>Lower>>>5>>>7
Contains>>>def
Contains>>>deF
Generate

Output
abghijklmnopqrstuvwxyz
abgHIJKLMNOPQRstuvwxyz
abgHIjkLMNOPQRstuvwxyz
Substring not found!
Substring not found!
Your activation key is: abgHIjkLMNOPQRstuvwxyz

Explanation
1.	Slice>>2>>6 
abcdefghijklmnopqrstuvwxyz becomes abghijklmnopqrstuvwxyz
2.	Flip>>>Upper>>>3>>>14
abghijklmnopqrstuvwxyz becomes abgHIJKLMNOPQRstuvwxyz
3.	Flip>>>Lower>>>5>>>7
abgHIJKLMNOPQRstuvwxyz becomes abgHIjkLMNOPQRstuvwxyz
4.	Contains>>>def
abgHIjkLMNOPQRstuvwxyz does not contain def
5.	Contains>>>deF
abgHIjkLMNOPQRstuvwxyz does not contain deF
The final activation key is abgHIjkLMNOPQRstuvwxyz
____________________________________________________________________________________________
Example_02

Input 
134softsf5ftuni2020rockz42
Slice>>>3>>>7
Contains>>>-rock
Contains>>>-uni-
Contains>>>-rocks
Flip>>>Upper>>>2>>>8
Flip>>>Lower>>>5>>>11
Generate

Output
134sf5ftuni2020rockz42
Substring not found!
Substring not found!
Substring not found!
134SF5FTuni2020rockz42
134SF5ftuni2020rockz42
Your activation key is: 134SF5ftuni2020rockz42

"""