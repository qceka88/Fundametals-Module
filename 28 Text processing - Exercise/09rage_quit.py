class Rage:

    def __init__(self, string):
        self.string = string

    def escalating(self):
        final_string = ''
        current_part = ''
        number = ''
        for index in range(len(self.string)):
            symbol = self.string[index]
            if not symbol.isdigit():
                current_part += symbol.upper()
            else:
                for num_index in range(index, len(self.string)):
                    if not self.string[num_index].isdigit():
                        break
                    number += self.string[num_index]
                final_string += current_part * int(number)
                current_part = ''
                number = ''

        return final_string

    def __repr__(self):
        unique_symbols = len(set(self.escalating()))
        return f'Unique symbols used: {unique_symbols}\n{self.escalating()}'


input_data = input()

raging = Rage(input_data)

print(raging)

#################################### TASK CONDITION ############################
"""
                        9.	 *Rage Quit
Every gamer knows what rage-quitting means. It's when you're just not good enough, 
and you blame everybody else for losing a game - you press the CAPS LOCK key on the 
keyboard and flood the chat with gibberish to show your frustration. 
Peter is a gamer, a bad one. When he rage-quits, he wants to be the most annoying 
kid on his team; he wants something truly spectacular. He asks for your help.
He'll give you a series of strings (containing only non-numerical characters) followed
by non-negative numbers (N), e.g., "a3". You need to convert the letters to uppercase 
for each string and print it repeatedly N times on the console. In the example, you need to write back "AAA".
First, on the output, you should print a statistic of the number of unique symbols
used (case-insensitive) in the format: "Unique symbols used {0}".
Next, print the rage message itself.
The strings and numbers will not be separated by anything. The input will always start with 
a non-numeric symbol, and for each string, there will be a corresponding number. 
The input will be given on a single line.
Input
•	The input data should be read from the console.
•	It consists of a single line holding a series of string-number sequences.
•	The input data will always be valid. There is no need to check it explicitly.
Output
•	The output should be printed on the console. It should consist of exactly two lines:
o	On the first line, print the number of unique symbols used in the message in the format described above.
o	On the second line, print the rage message.
Constraints
•	The count of string-number pairs will be in the range [1 … 20 000].
•	Each string will contain any character except digits. The length of each string will be in the range [1 … 20].
•	The repeat count for each string will be an integer in the range [0 … 20].
•	Allowed working time for your program: 0.3 seconds. Allowed memory: 64 MB.

____________________________________________________________________________________________
Example_01

Input
a3	

Output
Unique symbols used: 1

Explanation
AAA	We have just one string-number pair. The symbol is 'a', 
convert it to uppercase and repeat 3 times: AAA.
Only one symbol is used ('A').

____________________________________________________________________________________________
Example_02

Input
aSd2&5s@1

Output
Unique symbols used: 5
ASDASD&&&&&S@

Explanation
"aSd" is converted to "ASD" and repeated twice; "&" is repeated 5 times;
"s@" is converted to "S@" and repeated once.
5 symbols are used: 'A', 'S', 'D', '&' and '@'.

"""
