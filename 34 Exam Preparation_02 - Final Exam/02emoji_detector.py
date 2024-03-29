##################################### variant 01 #####################################

import re

input_line = input()
pattern_emoji = r'((?P<end>\*{2}|\:{2})([A-Z][a-z]{2,})(?P=end))'
pattern_digit = r'\d'
match_emoji = re.findall(pattern_emoji, input_line)
match_digit = re.findall(pattern_digit, input_line)

coolnes = 1

for number in match_digit:
    coolnes *= int(number)
print(f"Cool threshold: {coolnes}")
print(f"{len(match_emoji)} emojis found in the text. The cool ones are:")
for founded_emoji in match_emoji:
    emoji = founded_emoji[0]
    cool_meter = sum([ord(char) for char in emoji[2:-2]])
    if cool_meter > coolnes:
        print(emoji)


##################################### variant 02 #####################################

import re


class Regex:

    def __init__(self, some_pattern, some_text):
        self.some_pattern = some_pattern
        self.some_text = some_text

    def regex_action(self):
        match = re.findall(self.some_pattern, self.some_text)
        return match


class CoolThreshold:
    __pattern_digit = r'\d'

    def __init__(self, some_text):
        self.some_text = some_text
        self.message = ''

    def coolnes_calculation(self):
        coolnes_list = Regex(CoolThreshold.__pattern_digit, self.some_text).regex_action()
        coolnes = 1
        for number in coolnes_list:
            coolnes *= int(number)
        self.message += f"Cool threshold: {coolnes}\n"
        return coolnes

    def return_data(self):
        return self.message


class Emojis:
    __pattern_emoji = r'((?P<end>\*{2}|\:{2})([A-Z][a-z]{2,})(?P=end))'

    def __init__(self, some_number, some_text):
        self.some_number = some_number
        self.some_text = some_text
        self.message = ''

    def find_emojis(self):
        emoji_list = Regex(Emojis.__pattern_emoji, self.some_text).regex_action()
        self.message += f"{len(emoji_list)} emojis found in the text. The cool ones are:\n"
        for founded_emoji in emoji_list:
            emoji = founded_emoji[0]
            cool_meter = sum([ord(char) for char in emoji[2:-2]])
            if cool_meter > self.some_number:
                self.message += f'{emoji}\n'

    def return_data(self):
        return self.message


class Main:

    def __init__(self):
        self.some_input = input()
        self.log_file = ''

    def fill_log_file(self):
        cool_object = CoolThreshold(self.some_input)
        cool_object.coolnes_calculation()
        self.log_file += cool_object.return_data()
        emoji_object = Emojis(cool_object.coolnes_calculation(), self.some_input)
        emoji_object.find_emojis()
        self.log_file += emoji_object.return_data()

    def __repr__(self):
        return f'{self.log_file}'


output = Main()
output.fill_log_file()
print(output)


#################################### TASK CONDITION ############################
"""
                            Problem 2 - Emoji Detector
Problem for exam preparation for the Programming Fundamentals Course @SoftUni.
Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2302#1.

Your task is to write a program that extracts emojis from 
a text and find the threshold based on the input.
You have to get your cool threshold. It is obtained by multiplying 
all the digits found in the input.  The cool threshold could be a huge number, so be mindful.
An emoji is valid when:
•	It is surrounded by 2 characters, either "::" or "**"
•	It is at least 3 characters long (without the surrounding symbols)
•	It starts with a capital letter
•	Continues with lowercase letters only
Examples of valid emojis: ::Joy::, **Banana**, ::Wink::
Examples of invalid emojis: ::Joy**, ::fox:es:, **Monk3ys**, :Snak::Es::
You need to count all valid emojis in the text and calculate their coolness. 
The coolness of the emoji is determined by summing all the ASCII values of all letters in the emoji. 
Examples: ::Joy:: - 306, **Banana** - 577, ::Wink:: - 409
You need to print the result of the cool threshold and, after that to take 
all emojis out of the text, count them and print only the cool ones on the console.
Input
•	On the single input, you will receive a piece of string. 
Output
•	On the first line of the output, print the obtained Cool threshold in the format:
"Cool threshold: {coolThresholdSum}"
•	On the following line, print the count of all emojis found in the text in format:
"{countOfAllEmojis} emojis found in the text. The cool ones are:
{cool emoji 1}
{cool emoji 2}
…
{cool emoji N}"
Constraints
There will always be at least one digit in the text!


!!!!!!!!!!!!!!!!!NOTE!!!!! all example inputs must be on single line, 
now are separated on several lines for easy reading!!!!!!!!!!!!!!
____________________________________________________________________________________________
Example_01

Input 
In the Sofia Zoo there are 311 animals in total!
::Smiley:: This includes 3 **Tigers**, 1 ::Elephant:, 
12 **Monk3ys**, a **Gorilla::, 5 ::fox:es: and 21 different types of 
:Snak::Es::. ::Mooning:: **Shy**

Output
Cool threshold: 540
4 emojis found in the text. The cool ones are:
::Smiley:: 
**Tigers** 
::Mooning::


Explanation
You can see all the valid emojis in green. 
There are various reasons why the rest are not valid, examine 
them carefully. The "cool threshold" is 3*1*1*3*1*1*2*3*5*2*1 = 540.
::Smiley:: -> 83 + 109 + 105 + 108 + 101 + 121 = 627 > 540 -> cool
**Tigers** -> 84 + 105 + 103 + 101 + 114 + 115 = 622 > 540 -> cool
::Mooning:: -> 77 + 111 + 111 + 110 + 105 + 110 + 103 = 727 > 540 -> cool 
**Shy** -> 83 + 104 + 121 = 308 < 540 -> not cool
In the end, we print the count of all valid emojis found and each of the cool ones on a new line.
____________________________________________________________________________________________
Example_02

Input 
5, 4, 3, 2, 1, go! The 1-th 
consecutive banana-eating contest has begun! 
::Joy:: **Banana** ::Wink:: **Vali** ::valid_emoji::

Output
Cool threshold: 120
4 emojis found in the text. The cool ones are:
::Joy::
**Banana**
::Wink::
**Vali**
____________________________________________________________________________________________
Example_03

Input 
It is a long established fact that 1 a reader will be distracted by 
9 the readable content of a page when looking at its layout. 
The point of using ::LoremIpsum:: is that it has a more-or-less normal 3 
distribution of 8 letters, as opposed to using 'Content here, content 99 here', 
making it look like readable **English**.

Output
Cool threshold: 17496
1 emojis found in the text. The cool ones are:

Explanation
You can see **English** is a valid emoji, but the sum of 
ASCII is not bigger than the cool threshold. That's why we don't print anything in the end.

"""