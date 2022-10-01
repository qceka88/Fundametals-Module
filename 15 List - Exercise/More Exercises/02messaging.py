numbers = input().split()
message = [symbol for symbol in input()]
hidden_message = []
for number in numbers:
    index = sum([int(digit) for digit in number])
    if index >= len(message):
        index -= len(message)
    letter = message.pop(index)
    hidden_message.append(letter)

print(*hidden_message, sep='')

#################################### TASK CONDITION ############################
"""
                     2.	Messaging
On the first line, you will receive a sequence of numbers separated by a single space. 
On the second line, you will receive a string.
Your task is to write a program that sends a message only using chars from the given string.
Each char the program adds to the message should be found by its index. 
The index you are looking for is the sum of a number's digits from the first sequence. 
If the index is greater than the length of the text, continue counting from the beginning 
(so that you always have a valid index). When you find a char, you should add it to the 
message and remove it from the string. It means that for the following index, 
the text will contain one character less. Print the final message.


____________________________________________________________________________________________
Example_01

Input
9992 562 8933
This is some message for you

Output
hey
____________________________________________________________________________________________
Example_02

Input
2 122 1123 1321 9 17211
87j973u59dg37e725!

Output
judge!

"""
