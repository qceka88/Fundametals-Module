class Letters:

    def __init__(self, words_list):
        self.words_list = words_list

    def upper_position(self, letter):
        position = ord(letter) - 64
        return position

    def lower_position(self, letter):
        position = ord(letter) - 96
        return position

    def change_of_letters(self):
        total_sum = 0
        for word in self.words_list:
            first = word[0]
            last = word[-1]
            current_sum = int(word[1:-1])
            if first.isupper():
                position_of_letter = self.upper_position(first)
                current_sum /= position_of_letter
            elif first.islower():
                position_of_letter = self.lower_position(first)
                current_sum *= position_of_letter
            if last.isupper():
                position_of_letter = self.upper_position(last)
                current_sum -= position_of_letter
            elif last.islower():
                position_of_letter = self.lower_position(last)
                current_sum += position_of_letter
            total_sum += current_sum
        return total_sum

    def __repr__(self):
        return f'{self.change_of_letters():.2f}'


sequence = [word.strip() for word in input().split()]

number = Letters(sequence)

print(number)





#################################### TASK CONDITION ############################
"""
                               8.	 *Letters Change Numbers
John invented a game with numbers and letters from the English alphabet. The game was simple.
You receive a string consisting of a number between two letters. For the given string, 
you should perform different mathematical operations to achieve a result:
•	First, if the letter in front of the number is:
o	Uppercase: divide the number by the letter's position in the alphabet (starting from 1)
o	Lowercase: multiply the number with the letter's position in the alphabet (starting from 1)
•	Next, if the letter after the number is:
o	Uppercase: subtract its position from the resulting number (starting from 1)
o	Lowercase: add its position to the resulting number (starting from 1)
The game was too easy for John. He decided to complicate it by doing the same calculations 
to multiple strings keeping track of only the total sum of all results.
Once he started to solve this with more strings and bigger numbers, 
it became quite hard to do it only in his mind. He kindly asks you to write a program that 
performs the operations described above and sums the final results of each string.
Input
•	The input comes from the console as a single line, holding a sequence of strings
•	Strings are separated by one or more white spaces
•	The input data will always be valid. There is no need to check it explicitly
Output
•	Print at the console a single number: 
o	The total sum of all processed numbers, formatted to the second decimal separator
Constraints
•	The count of the strings will be in the range [1 … 10]
•	The numbers between the letters will be integers in the range [1 … 2 147 483 647]
•	Time limit: 0.3 sec. Memory limit: 16 MB

____________________________________________________________________________________________
Example_01

Input
A12b s17G

Output
330.00

Explaining
12/1=12, 12+2=14, 17*19=323, 323–7=316, 14+316=330

____________________________________________________________________________________________
Example_02

Input
P34562Z q2576f   H456z

Output
46015.12

____________________________________________________________________________________________
Example_03

Input
a1A

Output
0.00


"""
