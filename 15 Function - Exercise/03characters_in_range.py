def characters(first, second):
    start = ord(first)
    end = ord(second)
    character_list = []
    for num in range(start+1, end):
        character_list.append(chr(num))
    return character_list

first_character = input()
second_character = input()

result = characters(first_character,second_character)

print(*result)




#################################### TASK CONDITION ############################
"""
                     3. Characters in Range
Write a function that receives two characters and returns a single
string with all the characters in between them (according to the ASCII code),
 eparated by a single space. Print the result on the console.


____________________________________________________________________________________________
Example_01

Input
a
d

Output
b c


____________________________________________________________________________________________
Example_02

Input
#
:

Output
$ % & ' ( ) * + , - . / 0 1 2 3 4 5 6 7 8 9


____________________________________________________________________________________________
Example_03

Input
#
C

Output
$ % & ' ( ) * + , - . / 0 1 2 3 4 5 6 7 8 9 : ; < = > ? @ A B

"""
