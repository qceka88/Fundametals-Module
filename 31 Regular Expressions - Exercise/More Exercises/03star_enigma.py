################################# variant 01 #################################
import re

number_of_messages = int(input())
key_pattern = r'(?i)[star]'  # (?i) == flags = re.IGNORECASE
info_pattern = r'@([A-Z][a-z]*)[^\@\-\!\:\>]*:(\d+)[^\@\-\!\:\>]*!([A|D])![^\@\-\!\:\>]*->(\d+)'
planets = {'Attacked': [], 'Destroyed': []}

for message in range(number_of_messages):
    secret_message = input()
    match_key = re.findall(key_pattern, secret_message)
    decrypted_message = ''
    for character in secret_message:
        new_character = chr(ord(character) - len(match_key))
        decrypted_message += new_character
    extract_info = re.search(info_pattern, decrypted_message)
    if extract_info:
        name = extract_info.group(1)
        command = extract_info.group(3)
        if command == 'A':
            planets['Attacked'].append(name)
        elif command == 'D':
            planets['Destroyed'].append(name)

for type, names in planets.items():
    print(f"{type} planets: {len(names)}")
    for name in sorted(names):
        print(f"-> {name}")

################################# variant 02 #################################

import re


class MoreMagic:

    def __init__(self, some_text):
        self.some_text = some_text

    def regex_key(self):
        pattern = r'(?i)[star]'  # (?i) = flags = re.IGNORECASE
        extracted_key = re.findall(pattern, self.some_text)
        return extracted_key

    def regex_info(self):
        pattern = r'@([A-Z][a-z]*)[^\@\-\!\:\>]*:(\d+)[^\@\-\!\:\>]*!([A|D])![^\@\-\!\:\>]*->(\d+)'
        extract_info = re.search(pattern, self.some_text)
        if extract_info:
            return extract_info
        return None


class MagicAction:

    def __init__(self, some_string, planets_dict):
        self.some_string = some_string
        self.planets_dict = planets_dict

    def decrypt_message(self):
        key_object = MoreMagic(self.some_string)
        key = key_object.regex_key()
        decrypted_message = ''
        for character in self.some_string:
            new_character = chr(ord(character) - len(key))
            decrypted_message += new_character
        return decrypted_message

    def separate_data(self):
        info_object = MoreMagic(self.decrypt_message())
        info = info_object.regex_info()
        if info is not None:
            name = info.group(1)
            command = info.group(3)
            if command == 'A':
                self.planets_dict['Attacked'].append(name)
            elif command == 'D':
                self.planets_dict['Destroyed'].append(name)
        return self.planets_dict

    def output_data(self):
        return self.separate_data()


class Printing:

    def __init__(self, some_dict):
        self.some_dict = some_dict

    def print_action(self):
        for type, names in self.some_dict.items():
            print(f"{type} planets: {len(names)}")
            for name in sorted(names):
                print(f"-> {name}")


number_of_messages = int(input())

planets_data = {'Attacked': [], 'Destroyed': []}

for message in range(number_of_messages):
    secret_message = input()
    output = MagicAction(secret_message, planets_data)
    planets_data = output.output_data()

represent = Printing(planets_data)
represent.print_action()

#################################### TASK CONDITION ############################
"""
                              3.	Star Enigma
The war is in its peak, but you, young Padawan, can turn the tides with your 
programming skills. You are tasked to create a program to decrypt the messages 
of The Order and prevent the death of hundreds of lives. You will receive 
several messages, which are encrypted using the legendary star enigma.
You should decrypt the messages, following these rules:
To properly decrypt a message, you should count all the letters 
[s, t, a, r] – case insensitive and remove the count from the current 
ASCII value of each symbol of the encrypted message.
After decryption:
Each message should have a planet name, population, attack type 
('A', as attack or 'D', as destruction) and soldier count.
The planet name starts after '@' and contains only letters from the Latin alphabet. 
The planet population starts after ':' and is an Integer;
The attack type may be "A"(attack) or "D"(destruction) and must be surrounded by "!" (exclamation mark).
The soldier count starts after "->" and should be an Integer.
The order in the message should be: planet name -> planet population -> attack type -> soldier count.
Each part can be separated from the others by any character except: '@', '-', '!', ':' and '>'.
Input / Constraints
•	The first line holds n – the number of messages– integer in range [1…100];
•	On the next n lines, you will be receiving encrypted messages.
Output
After decrypting all messages, you should print the decrypted information in the following format:
First print the attacked planets, then the destroyed planets.
"Attacked planets: {attackedPlanetsCount}"
"-> {planetName}"
"Destroyed planets: {destroyedPlanetsCount}"
"-> {planetName}"
The planets should be ordered by name alphabetically.

____________________________________________________________________________________________
Example_01

Input
2
STCDoghudd4=63333$D$0A53333
EHfsytsnhf?8555&I&2C9555SR	

Output
Attacked planets: 1
-> Alderaa
Destroyed planets: 1
-> Cantonica	

Explanation
We receive two messages, to decrypt them we calculate the key:
First message has decryption key 3. 
So we substract from each characters code 3.
PQ@Alderaa1:30000!A!->20000
The second message has key 5.
@Cantonica:3000!D!->4000NM
Both messages are valid and they contain planet,
 population, attack type and soldiers count. 
After decrypting all messages we print each
 planet according the format given.

____________________________________________________________________________________________
Example_02

Input
3
tt(''DGsvywgerx>6444444444%H%1B9444
GQhrr|A977777(H(TTTT
EHfsytsnhf?8555&I&2C9555SR	

Output
Attacked planets: 0
Destroyed planets: 2
-> Cantonica
-> Coruscant

Explanation
We receive three messages.
Message one is decrypted with key 4:
pp$##@Coruscant:2000000000!D!->5000
Message two is decrypted with key 7:
@Jakku:200000!A!MMMM
This is invalid message, missing soldier count, so we continue.
The third message has key 5.
@Cantonica:3000!D!->4000NM




"""
