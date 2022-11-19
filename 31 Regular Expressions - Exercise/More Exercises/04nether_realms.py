##################################### variant 01 #####################################

import re


class Regex:

    def __init__(self, some_text):
        self.some_text = some_text

    def regex_name(self):
        name_pattern = r',*([^\,]+),*'
        match_names = re.findall(name_pattern, self.some_text)
        return match_names

    def regex_health(self):
        health_pattern = r'([^\+\-\/\*\.\,\d])'
        health_match = re.findall(health_pattern, self.some_text)
        return health_match

    def regex_damage(self):
        damage_pattern = r'((\-?)(\d+(\.?\d+)?))'
        damage_match = re.findall(damage_pattern, self.some_text)
        return damage_match

    def regex_bonus(self):
        bonus_pattern = r'(\*|\/)'
        bonus_match = re.findall(bonus_pattern, self.some_text)
        return bonus_match


class Extracting:

    def __init__(self, some_name, some_dict):
        self.some_name = some_name
        self.some_dict = some_dict

    def stats_extract(self):
        stats = Regex(self.some_name)
        health = sum([ord(char) for char in stats.regex_health()])
        damage = sum([float(num[0]) for num in stats.regex_damage()])
        bonus = stats.regex_bonus()
        for action in bonus:
            if action == '*':
                damage *= 2
            elif action == '/':
                damage /= 2
        self.some_dict[self.some_name] = [health, damage]
        return self.some_dict

    def returning_data(self):
        return self.stats_extract()


class Information:

    def __init__(self, some_input):
        self.some_input = some_input
        self.demons_stats = {}

    def extract_data(self):
        names_object = Regex(self.some_input)
        names_of_demons = names_object.regex_name()
        for demon in names_of_demons:
            demon_name = demon.strip()
            extract_object = Extracting(demon_name, self.demons_stats)
            self.demons_stats = extract_object.returning_data()
        return self.demons_stats

    def printing(self):
        for name, stats in sorted(self.extract_data().items(), key=lambda x: x[0]):
            print(f"{name} - {stats[0]} health, {stats[1]:.2f} damage")


output = Information(input()).printing()


##################################### variant 02 #####################################

import re

input_line = input()

name_pattern = r',*([^\,]+),*'
health_pattern = r'([^\+\-\/\*\.\,\d])'
damage_pattern = r'((\-?)(\d+(\.?\d+)?))'
bonus_pattern = r'(\*|\/)'
demon_names = re.findall(name_pattern, input_line)
demons_stats = {}
for demon in demon_names:
    demon_name = demon.strip()
    health_match = re.findall(health_pattern, demon_name)
    health = sum([ord(char) for char in health_match])
    damage_match = re.findall(damage_pattern, demon_name)
    damage = sum([float(num[0]) for num in damage_match])
    bonus_match = re.findall(bonus_pattern, demon_name)
    for action in bonus_match:
        if action == '*':
            damage *= 2
        elif action == '/':
            damage /= 2
    demons_stats[demon_name] = [health, damage]

for name, stats in sorted(demons_stats.items()):
    print(f"{name} - {stats[0]} health, {stats[1]:.2f} damage")


#################################### TASK CONDITION ############################
"""
                      4.	Nether Realms
Mighty battle is coming. In the stormy nether realms, demons are fighting 
against each other for supremacy in a duel from which only one will survive. 
Your job, however is not so exciting. You are assigned to sign in all the participants 
in the nether realm's mighty battle's demon book, which of course is sorted alphabetically. 
A demon's name contains his health and his damage. 
The sum of the asci codes of all characters (excluding numbers (0-9), arithmetic 
symbols ('+', '-', '*', '/') and delimiter dot ('.')) gives a demon's total health. 
The sum of all numbers in his name forms his base damage. Note that you should consider
the plus '+' and minus '-' signs (e.g. +10 is 10 and -10 is -10). However, there are 
some symbols ('*' and '/') that can further alter the base damage by multiplying or
dividing it by 2 (e.g. in the name "m15*/c-5.0", the base damage is 15 + (-5.0) = 10 and 
then you need to multiply it by 2 (e.g. 10 * 2 = 20) and then divide it by 2 (e.g. 20 / 2 = 10)). 
So, multiplication and division are applied only after all numbers are included 
in the calculation and in the order they appear in the name. 
You will get all demons on a single line, separated by commas and zero or more blank spaces. 
Sort them in alphabetical order and print their names along their health and damage. 
Input
The input will be read from the console. The input consists of a single 
line containing all demon names separated by commas and zero or more spaces 
in the format: "{demon name}, {demon name}, … {demon name}"
Output
Print all demons sorted by their name in ascending order, each on a separate line in the format:
•	"{demon name} - {health points} health, {damage points} damage"
Constraints
•	A demon's name will contain at least one character
•	A demon's name cannot contain blank spaces ' ' or commas ','
•	A floating point number will always have digits before and after its decimal separator
•	Number in a demon's name is considered everything that is a valid integer or floating 
point number (with dot '.' used as separator). For example, 
all these are valid numbers: '4', '+4', '-4', '3.5', '+3.5', '-3.5' 

____________________________________________________________________________________________
Example_01

Input
M3ph-0.5s-0.5t0.0**	

Output
M3ph-0.5s-0.5t0.0** - 524 health, 8.00 damage

Explanation
M3ph-0.5s-0.5t0.0**:
Health = 'M' + 'p' + 'h' + 's' + 't' = 524 health.
Damage = (3 + (-0.5) + (-0.5) + 0.0) * 2 * 2 = 8 damage.

____________________________________________________________________________________________
Example_02

Input
M3ph1st0**, Azazel

Output
Azazel - 615 health, 0.00 damage 
M3ph1st0** - 524 health, 16.00 damage


Explanation
Azazel: 
Health - 'A' + 'z' + 'a' + 'z' + 'e' + 'l' = 615 health. Damage - no digits = 0 damage.

M3ph1st0**:
Health - 'M' + 'p' + 'h' + 's' + 't' = 524 health.
Damage - (3 + 1 + 0) * 2 * 2 = 16 damage.

____________________________________________________________________________________________
Example_03

Input
Gos/ho

Output
Gos/ho - 512 health, 0.00 damage


"""
