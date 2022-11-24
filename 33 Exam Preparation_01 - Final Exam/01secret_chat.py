##################################### variant 01 #####################################
class Secrets:

    def __init__(self, some_input, message):
        self.some_input = some_input
        self.message = message

    def action(self):
        data = self.some_input.split(':|:')
        action = data[0]
        substring = data[1]
        if action == 'InsertSpace':
            index = int(substring)
            self.message = self.insert_space(index)
        elif action == 'Reverse':
            if substring not in self.message:
                return 'error'
            self.message = self.reverse(substring)
        elif action == 'ChangeAll':
            old_part = substring
            new_part = data[2]
            self.message = self.change_all(old_part, new_part)
        return self.message

    def insert_space(self, some_index):
        string = self.message[:some_index] + ' ' + self.message[some_index:]
        return string

    def reverse(self, some_string):
        string = self.message.replace(some_string, '', 1)
        string += some_string[::-1]
        return string

    def change_all(self, old, new):
        string = self.message.replace(old, new)
        return string

    def return_to_main(self):
        return self.action()


class Main:

    def __init__(self, text):
        self.text = text

    def input_data(self):
        while True:
            command = input()
            if command == 'Reveal':
                break
            command_object = Secrets(command, self.text).return_to_main()
            if command_object != 'error':
                self.text = command_object
            print(command_object)
        print(f'You have a new text message: {self.text}')


initial_message = input()
output = Main(initial_message).input_data()

##################################### variant 02 #####################################
message = input()
command = input()

while command != 'Reveal':
    input_data = command.split(":|:")
    action = input_data[0]
    substring = input_data[1]
    if action == 'InsertSpace':
        index = int(substring)
        message = message[:index] + ' ' + message[index:]
        print(message)
    elif action == 'Reverse':
        if substring not in message:
            print('error')
        else:
            reversed_string = substring[::-1]
            message = message.replace(substring, '', 1)
            message += reversed_string
            print(message)
    elif action == 'ChangeAll':
        if substring in message:
            new_string = input_data[2]
            message = message.replace(substring, new_string)
            print(message)

    command = input()
print(f"You have a new text message: {message}")


#################################### TASK CONDITION ############################
"""
                               Problem 1 - Secret Chat
Problem for exam preparation for the Programming Fundamentals Course @SoftUni.
Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2307#0.

You have plenty of free time, so you decide to write a program that 
conceals and reveals your received messages. Go ahead and type it in!
On the first line of the input, you will receive the concealed message. 
After that, until the "Reveal" command is given, you will receive strings 
with instructions for different operations that need to be performed upon 
the concealed message to interpret it and reveal its actual content. 
There are several types of instructions, split by ":|:"
•	"InsertSpace:|:{index}":
o	Inserts a single space at the given index. The given index 
will always be valid.
•	"Reverse:|:{substring}":
o	If the message contains the given substring, cut it out, 
reverse it and add it at the end of the message. 
o	If not, print "error".
o	This operation should replace only the first occurrence of the 
given substring if there are two or more occurrences.
•	"ChangeAll:|:{substring}:|:{replacement}":
o	Changes all occurrences of the given substring with the replacement text.
Input / Constraints
•	On the first line, you will receive a string with a message.
•	On the following lines, you will be receiving commands, split by ":|:".
Output
•	After each set of instructions, print the resulting string. 
•	After the "Reveal" command is received, print this message:
"You have a new text message: {message}"

____________________________________________________________________________________________
Example_01

Input
heVVodar!gniV
ChangeAll:|:V:|:l
Reverse:|:!gnil
InsertSpace:|:5
Reveal

Output
hellodar!gnil
hellodarling!
hello darling!
You have a new text message: hello darling!


Explanation
ChangeAll:|:V:|:l
heVVodar!gniV -> hellodar!gnil 
(We replace all occurrences of "V" with "l")
Reverse:|:!gnil
hellodar!gnil -> !gnil -> ling! -> hellodarling! 
(We reverse !gnil to ling! And put it at the end of the string)
InsertSpace:|:5
hellodarling! -> hello.darling! (We insert a space at index 5)
Finally, after receiving the "Reveal" command, we print the resulting message.

____________________________________________________________________________________________
Example_02

Input
ChangeAll:|:i:|:o
Reverse:|:?uoy
Reverse:|:jd
InsertSpace:|:3
InsertSpace:|:7
Reveal

Output
Howare?uoy
Howareyou?
error
How areyou?
How are you?
You have a new text message: How are you?

"""
