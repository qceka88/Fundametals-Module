##################################### variant 01 #####################################


import re

number_messages = int(input())
pattern = r'^(?P<sep>\$|\%)([A-Z][a-z]{2,})(?P=sep): \[(\d+)]\|\[(\d+)]\|\[(\d+)]\|$'

for number in range(number_messages):
    current_input = input()
    match = re.findall(pattern, current_input)
    if not match:
        print("Valid message not found!")
    else:
        tag_decrypted = match[0][1]
        new_message = chr(int(match[0][2])) + chr(int(match[0][3])) + chr(int(match[0][4]))
        print(f"{tag_decrypted}: {new_message}")

##################################### variant 02 #####################################

import re


class Regex:

    def __init__(self, some_text):
        self.some_text = some_text

    def action_regex(self):
        match = re.findall(r'^(?P<sep>\$|\%)([A-Z][a-z]{2,})(?P=sep): \[(\d+)]\|\[(\d+)]\|\[(\d+)]\|$', self.some_text)
        if match:
            return match
        return False


class CheckMessage:

    def __init__(self, some_text):
        self.some_text = some_text
        self.log = ''

    def extract_data(self):
        extract = Regex(self.some_text).action_regex()
        if extract is False:
            self.log = f"Valid message not found!\n"
        else:
            tag_decrypted = extract[0][1]
            new_message = chr(int(extract[0][2])) + chr(int(extract[0][3])) + chr(int(extract[0][4]))
            self.log = f"{tag_decrypted}: {new_message}\n"

    def return_data(self):
        return self.log


class Main:

    def __init__(self):
        self.messages_number = int(input())
        self.log_file = ''

    def decrypting_messages(self):
        for number in range(self.messages_number):
            current_input = input()
            check = CheckMessage(current_input)
            check.extract_data()
            self.log_file += check.return_data()

    def __repr__(self):
        return f"{self.log_file}"


output = Main()
output.decrypting_messages()
print(output)



#'''' Problem conditions are in .docx .jpg files!'''