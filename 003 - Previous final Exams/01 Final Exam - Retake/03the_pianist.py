def add_piece(music_list, song, information):
    new_singer = information[2]
    new_key = information[3]
    if song not in music_list:
        music_list[song] = {'composer': new_singer, 'key': new_key}
        print(f'{song} by {new_singer} in {new_key} added to the collection!')
    else:
        print(f"{song} is already in the collection!")
    return music_list


def remove_piece(music_list, song):
    if song not in music_list:
        print(f"Invalid operation! {song} does not exist in the collection.")
    else:
        del music_list[song]
        print(f"Successfully removed {song}!")
    return music_list


def change_key(music_list, song, information):
    new_key = information[2]
    if song not in music_list:
        print(f"Invalid operation! {song} does not exist in the collection.")
    else:
        music_list[song]['key'] = new_key
        print(f"Changed the key of {song} to {new_key}!")
    return music_list


discography = {}

number_of_pieces = int(input())

for song in range(number_of_pieces):
    piece, composer, key = input().split('|')

    if piece not in discography:
        discography[piece] = {'composer': composer, 'key': key}

while True:
    input_data = input()
    if input_data == 'Stop':
        break

    data = input_data.split('|')
    command = data[0]
    piece = data[1]

    if command == 'Add':
        discography = add_piece(discography, piece, data)
    elif command == 'Remove':
        discography = remove_piece(discography, piece)
    elif command == 'ChangeKey':
        discography = change_key(discography, piece, data)

for piece, info in discography.items():
    composer = info['composer']
    key = info['key']
    print(f"{piece} -> Composer: {composer}, Key: {key}")

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