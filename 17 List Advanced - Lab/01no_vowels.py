########################### variant 01 ##########################
initial_string = input()

avoid_letters = ['a', 'o', 'u', 'e', 'i']

final_stirng = ''

for letter in initial_string:
    if letter.lower() not in avoid_letters:
        final_stirng += letter

print(final_stirng)

########################### variant 02 ##########################

initial_string = input()
avoid_letters = ['a', 'o', 'u', 'e', 'i']
print(''.join(letter for letter in initial_string if letter.lower() not in avoid_letters))



#################################### TASK CONDITION ############################
"""
1.	No Vowels
Using comprehension, write a program that receives a 
text and removes all its vowels, case insensitive. 
Print the new text string after removing the vowels. 
The vowels that should be considered are 'a', 'o', 'u', 'e', 'i'.


____________________________________________________________________________________________
Example_01

Input
Python

Output
Pythn


____________________________________________________________________________________________
Example_02

Input
ILovePython

Output
LvPythn


"""
