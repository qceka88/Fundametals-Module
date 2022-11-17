################################  Variant 01 ################################


from collections import defaultdict
import re

participants = input().split(', ')

name_pattern = r'[A-Za-z]'
numbers_pattern = r'\d'

final_result = defaultdict(int)

while True:
    input_data = input()
    if input_data == 'end of race':
        break
    name_match = re.findall(name_pattern, input_data)
    number_match = re.findall(numbers_pattern, input_data)

    current_name = ''.join(letter for letter in name_match)
    current_number = sum(int(num) for num in number_match)
    if current_name in participants:
        final_result[current_name] += current_number

winners = sorted(final_result.items(), key=lambda x: -x[1])

print(f'1st place: {winners[0][0]}')
print(f'2nd place: {winners[1][0]}')
print(f'3rd place: {winners[2][0]}')

################################  Variant 02 ################################


from collections import defaultdict
import re


class Regex:

    def __init__(self, text):
        self.text = text

    def regex_name(self):
        name_match = re.findall(r'[A-Za-z]', self.text)
        return name_match

    def regex_distance(self):
        distance_match = re.findall(r'\d', self.text)
        return distance_match


class Extracting:

    def __init__(self, data):
        self.data = data
        self.regex = Regex(self.data)

    def name(self):
        current_name = ''.join(letter for letter in self.regex.regex_name())
        return current_name

    def distance(self):
        current_number = sum(int(num) for num in self.regex.regex_distance())
        return str(current_number)

    def returning_data(self):
        return (self.name(), self.distance())


class Winners:

    def __init__(self, participants):
        self.participants = participants

    def finalists(self):
        winners = sorted(self.participants.items(), key=lambda x: -x[1])
        return winners

    def printing(self):
        first = self.finalists()[0][0]
        second = self.finalists()[1][0]
        third = self.finalists()[2][0]
        print(f'1st place: {first}')
        print(f'2nd place: {second}')
        print(f'3rd place: {third}')


participants = input().split(', ')

final_result = defaultdict(int)

while True:
    input_data = input()
    if input_data == 'end of race':
        break

    data = Extracting(input_data)
    name = data.returning_data()[0]
    distance = int(data.returning_data()[1])
    if name in participants:
        final_result[name] += distance

finals = Winners(final_result)
finals.printing()

#################################### TASK CONDITION ############################
"""
                              1.	Race
Write a program that processes information about a race.
On the first line you will be given list of participants separated by ", ".
On the next few lines until you receive a line "end of race" you will be given some 
info which will be some alphanumeric characters. In between them you could have some
extra characters which you should ignore. For example: "G!32e%o7r#32g$235@!2e". 
The letters are the name of the person and the sum of the digits is the distance he ran. 
So here we have George who ran 29 km. Store the information about the person only if the 
list of racers contains the name of the person. If you receive the same person more than once
just add the distance to his old distance. At the end print the top 3 racers ordered 
by distance in descending in the format:

"1st place: {first racer}
2nd place: {second racer}
3rd place: {third racer}"

____________________________________________________________________________________________
Example

Input
George, Peter, Bill, Tom
G4e@55or%6g6!68e!!@
R1@!3a$y4456@
B5@i@#123ll
G@e54o$r6ge#
7P%et^#e5346r
T$o553m&6
end of race	

Output
1st place: George
2nd place: Peter
3rd place: Tom	


Explanation
On the 3rd input line we have Ray.
He is not in the list, so we do not count his result. 
The other ones are valid. George has total of 55 km, 
Peter has 25 and Tom has 19. We do not print Bill because he is on 4th place.


"""
