##################################### variant 01 #####################################

initial_spell = input()

while True:
    command = input()
    if command == "Abracadabra":
        # print(initial_spell)
        break

    data = command.split()
    action = data[0]

    if action == "Abjuration":
        initial_spell = initial_spell.upper()
        print(initial_spell)
    elif action == "Necromancy":
        initial_spell = initial_spell.lower()
        print(initial_spell)
    elif action == "Illusion":
        index, letter = int(data[1]), data[2]
        if index < 0 or index >= len(initial_spell):
            print("The spell was too weak.")
        else:
            initial_spell = initial_spell[:index] + letter + initial_spell[index + 1:]
            print("Done!")
    elif action == "Divination":
        first_substring, second_substring = data[1], data[2]
        if first_substring in initial_spell:
            initial_spell = initial_spell.replace(first_substring, second_substring)
            print(initial_spell)
    elif action == "Alteration":
        substring = data[1]
        if substring in initial_spell:
            initial_spell = initial_spell.replace(substring, '')
            print(initial_spell)
    else:
        print("The spell did not work!")


##################################### variant 02 #####################################


class Abjuration:

    def __init__(self, some_text):
        self.some_text = some_text

    def abjuration_method(self):
        self.some_text = self.some_text.upper()

    def return_data(self):
        return self.some_text


class Necromancy:

    def __init__(self, some_text):
        self.some_text = some_text

    def necromancy_method(self):
        self.some_text = self.some_text.lower()

    def return_data(self):
        return self.some_text


class Illusion:

    def __init__(self, some_text, some_data):
        self.some_text = some_text
        self.some_data = some_data
        self.message = ''

    def illusion_method(self):
        index, letter = int(self.some_data[1]), self.some_data[2]
        if index < 0 or index >= len(self.some_text):
            self.message += "The spell was too weak."
        else:
            self.some_text = self.some_text[:index] + letter + self.some_text[index + 1:]
            self.message += "Done!"

    def return_data(self):
        return self.some_text, self.message


class Divination:

    def __init__(self, some_text, some_data):
        self.some_text = some_text
        self.some_data = some_data

    def divination_method(self):
        first_substring, second_substring = self.some_data[1], self.some_data[2]
        if first_substring in self.some_text:
            self.some_text = self.some_text.replace(first_substring, second_substring)

    def return_data(self):
        return self.some_text


class Alteration:

    def __init__(self, some_text, some_data):
        self.some_text = some_text
        self.some_data = some_data

    def alteration_method(self):
        substring = self.some_data[1]
        if substring in self.some_text:
            self.some_text = self.some_text.replace(substring, '')

    def return_data(self):
        return self.some_text


class Actions:

    def __init__(self, some_spell, some_input):
        self.some_spell = some_spell
        self.some_input = some_input
        self.log = ""

    def choose_action(self):
        data = self.some_input.split()
        action = data[0]
        if action == "Abjuration":
            abjuration_object = Abjuration(self.some_spell)
            abjuration_object.abjuration_method()
            self.log += f"{abjuration_object.return_data()}\n"
            self.some_spell = abjuration_object.return_data()
        elif action == "Necromancy":
            necromancy_object = Necromancy(self.some_spell)
            necromancy_object.necromancy_method()
            self.log += f"{necromancy_object.return_data()}\n"
            self.some_spell = necromancy_object.return_data()
        elif action == "Illusion":
            illusion_object = Illusion(self.some_spell, data)
            illusion_object.illusion_method()
            self.log += f"{illusion_object.return_data()[1]}\n"
            self.some_spell = illusion_object.return_data()[0]
        elif action == "Divination":
            divination_object = Divination(self.some_spell, data)
            divination_object.divination_method()
            self.log += f"{divination_object.return_data()}\n"
            self.some_spell = divination_object.return_data()
        elif action == "Alteration":
            alteration_object = Alteration(self.some_spell, data)
            alteration_object.alteration_method()
            self.log += f"{alteration_object.return_data()}\n"
            self.some_spell = alteration_object.return_data()
        else:
            self.log += "The spell did not work!\n"

    def return_to_main(self):
        return self.some_spell, self.log


class Main:

    def __init__(self):
        self.initial_spell = input()
        self.log_file = ""

    def action_method(self):
        while True:
            command = input()
            if command == "Abracadabra":
                break
            action_object = Actions(self.initial_spell, command)
            action_object.choose_action()
            self.log_file += action_object.return_to_main()[1]
            self.initial_spell = action_object.return_to_main()[0]

    def __repr__(self):
        return f'{self.log_file}'


output = Main()
output.action_method()
print(output)

#'''' Problem conditions are in .jpg file and input data is in docx.file!'''