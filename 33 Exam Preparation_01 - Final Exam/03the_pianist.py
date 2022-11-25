##################################### variant 01 #####################################

number = int(input())

discography = {}

for current_input in range(number):
    piece, composer, key = input().split('|')
    discography[piece] = {'composer': composer, 'key': key}

while True:
    command = input()
    if command == 'Stop':
        break

    data = command.split('|')
    action = data[0]
    piece = data[1]

    if action == 'Add':
        if piece in discography:
            print(f"{piece} is already in the collection!")
        else:
            composer = data[2]
            key = data[3]
            discography[piece] = {'composer': composer, 'key': key}
            print(f"{piece} by {composer} in {key} added to the collection!")
    elif action == 'Remove':
        if piece not in discography:
            print(f"Invalid operation! {piece} does not exist in the collection.")
        else:
            discography.pop(piece)
            print(f"Successfully removed {piece}!")
    elif action == 'ChangeKey':
        if piece not in discography:
            print(f"Invalid operation! {piece} does not exist in the collection.")
        else:
            new_key = data[2]
            discography[piece]['key'] = new_key
            print(f"Changed the key of {piece} to {new_key}!")

for piece, data in discography.items():
    print(f"{piece} -> Composer: {data['composer']}, Key: {data['key']}")


##################################### variant 02 #####################################

class Add:

    def __init__(self, some_data, some_dict):
        self.some_data = some_data
        self.some_dict = some_dict

    def add_piece(self):
        piece, composer, key = self.some_data[1], self.some_data[2], self.some_data[3]
        if piece in self.some_dict:
            return f"{piece} is already in the collection!"
        else:
            self.some_dict[piece] = {'composer': composer, 'key': key}
            return f"{piece} by {composer} in {key} added to the collection!"

    def returning_data(self):
        return self.add_piece(), self.some_dict


class Remove:

    def __init__(self, some_data, some_dict):
        self.some_data = some_data
        self.some_dict = some_dict

    def remove_piece(self):
        piece = self.some_data[1]
        if piece not in self.some_dict:
            return f"Invalid operation! {piece} does not exist in the collection."
        else:
            del self.some_dict[piece]
            return f"Successfully removed {piece}!"

    def returning_data(self):
        return self.remove_piece(), self.some_dict


class ChangeKey:

    def __init__(self, some_data, some_dict):
        self.some_data = some_data
        self.some_dict = some_dict

    def change_key(self):
        piece, new_key = self.some_data[1], self.some_data[2]
        if piece not in self.some_dict:
            return f"Invalid operation! {piece} does not exist in the collection."
        else:
            self.some_dict[piece]['key'] = new_key
            return f"Changed the key of {piece} to {new_key}!"

    def returning_data(self):
        return self.change_key(), self.some_dict


class Action:

    def __init__(self, some_data, some_dict):
        self.some_data = some_data
        self.some_dict = some_dict

    def define_action(self):
        data = self.some_data.split('|')
        action = data[0]
        piece = data[1]
        if action == 'Add':
            adding = Add(data, self.some_dict)
            return adding.returning_data()
        elif action == 'Remove':
            removing = Remove(data, self.some_dict)
            return removing.returning_data()
        elif action == 'ChangeKey':
            changing = ChangeKey(data, self.some_dict)
            return changing.returning_data()


class Main:

    def __init__(self):
        self.discography = {}
        self.log_file = []

    def update_discography(self):
        number_of_pieces = int(input())
        for current_input in range(number_of_pieces):
            piece, composer, key = input().split('|')
            self.discography[piece] = {'composer': composer, 'key': key}

    def action_meth(self):
        while True:
            command = input()
            if command == 'Stop':
                break
            data = Action(command, self.discography).define_action()
            message = data[0]
            self.log_file.append(message)
            self.discography = data[1]

    def print_discography_information(self):
        print(*self.log_file, sep='\n')
        for piece, info in self.discography.items():
            print(f"{piece} -> Composer: {info['composer']}, Key: {info['key']}")


output = Main()
output.update_discography()
output.action_meth()
output.print_discography_information()

#################################### TASK CONDITION ############################
"""
                          Problem 3 - The Pianist
Problem for exam preparation for the Programming Fundamentals Course @SoftUni.
Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2525#2.

You are a pianist, and you like to keep a list of your favorite piano pieces. 
Create a program to help you organize it and add, change, remove pieces from it!
On the first line of the standard input, you will receive an integer n – the number 
of pieces you will initially have. On the next n lines, the pieces themselves will 
follow with their composer and key, separated by "|" in the following format: "{piece}|{composer}|{key}".
Then, you will be receiving different commands, each on a new line, separated by "|",
 until the "Stop" command is given:
•	"Add|{piece}|{composer}|{key}":
o	You need to add the given piece with the information about it to the other pieces and print:
"{piece} by {composer} in {key} added to the collection!"
o	If the piece is already in the collection, print:
"{piece} is already in the collection!"
•	"Remove|{piece}":
o	If the piece is in the collection, remove it and print:
"Successfully removed {piece}!"
o	Otherwise, print:
"Invalid operation! {piece} does not exist in the collection."
•	"ChangeKey|{piece}|{new key}":
o	If the piece is in the collection, change its key with the given one and print:
"Changed the key of {piece} to {new key}!"
o	Otherwise, print:
"Invalid operation! {piece} does not exist in the collection."
Upon receiving the "Stop" command, you need to print all pieces in your collection in the following format:
"{Piece} -> Composer: {composer}, Key: {key}"
Input/Constraints
•	You will receive a single integer at first – the initial number of pieces in the collection
•	For each piece, you will receive a single line of text with information about it.
•	Then you will receive multiple commands in the way described above until the command "Stop".
Output
•	All the output messages with the appropriate formats are described in the problem description.

____________________________________________________________________________________________
Example_01

Input
3
Fur Elise|Beethoven|A Minor
Moonlight Sonata|Beethoven|C# Minor
Clair de Lune|Debussy|C# Minor
Add|Sonata No.2|Chopin|B Minor
Add|Hungarian Rhapsody No.2|Liszt|C# Minor
Add|Fur Elise|Beethoven|C# Minor
Remove|Clair de Lune
ChangeKey|Moonlight Sonata|C# Major
Stop

Output
Sonata No.2 by Chopin in B Minor added to the collection!
Hungarian Rhapsody No.2 by Liszt in C# Minor added to the collection!
Fur Elise is already in the collection!
Successfully removed Clair de Lune!
Changed the key of Moonlight Sonata to C# Major!
Fur Elise -> Composer: Beethoven, Key: A Minor
Moonlight Sonata -> Composer: Beethoven, Key: C# Major
Sonata No.2 -> Composer: Chopin, Key: B Minor
Hungarian Rhapsody No.2 -> Composer: Liszt, Key: C# Minor


Explanaton
After we receive the initial pieces with their info, 
we start receiving commands. The first two commands are to 
add a piece to the collection, and since the pieces are not 
already added, we manage to add them. The third add command, 
however, attempts to add a piece, which is already in the collection, 
so we print a special message and don't add the piece.
 After that, we receive the remove command, and since the piece 
 is in the collection, we remove it successfully.
Finally, the last command says to change the key of a piece. 
Since the key is present in the collection, we modify its key.
We receive the Stop command, print the information about the pieces, and the program ends.

____________________________________________________________________________________________
Example_02

Input
4
Eine kleine Nachtmusik|Mozart|G Major
La Campanella|Liszt|G# Minor
The Marriage of Figaro|Mozart|G Major
Hungarian Dance No.5|Brahms|G Minor
Add|Spring|Vivaldi|E Major
Remove|The Marriage of Figaro
Remove|Turkish March
ChangeKey|Spring|C Major
Add|Nocturne|Chopin|C# Minor
Stop


Output
Spring by Vivaldi in E Major added to the collection!
Successfully removed The Marriage of Figaro!
Invalid operation! Turkish March does not exist in the collection.
Changed the key of Spring to C Major!
Nocturne by Chopin in C# Minor added to the collection!
Eine kleine Nachtmusik -> Composer: Mozart, Key: G Major
La Campanella -> Composer: Liszt, Key: G# Minor
Hungarian Dance No.5 -> Composer: Brahms, Key: G Minor
Spring -> Composer: Vivaldi, Key: C Major
Nocturne -> Composer: Chopin, Key: C# Minor

"""