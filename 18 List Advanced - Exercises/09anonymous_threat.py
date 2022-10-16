def merge(words_list, start, end):
    if start not in range(len(words_list)):
        start = 0
    if end not in range(len(words_list)):
        end = len(words_list)
    merged = [''.join(words_list[start:end + 1])]
    left = words_list[:start]
    right = words_list[end + 1:]
    words_list = left + merged + right
    return words_list


def divide(words_list, index, partition):
    word = words_list.pop(index)
    part = len(word) // partition
    new_parts = []
    start = 0
    end = 0
    for parts in range(partition - 1):
        end += part
        new_parts.append(word[start:end])
        start += part
    new_parts.append(word[end:])
    for idx, wrd in enumerate(new_parts):
        words_list.insert(index + idx, wrd)
    return words_list


initial_line = input().split()

while True:
    command = input()
    if command == '3:1':
        break

    input_data = command.split()
    order = input_data[0]
    start_index = int(input_data[1])
    end_index = int(input_data[2])

    if order == 'merge':
        initial_line = merge(initial_line, start_index, end_index)
    elif order == 'divide':
        initial_line = divide(initial_line, start_index, end_index)

print(*initial_line)



#################################### TASK CONDITION ############################
"""
                    9.	*Anonymous Threat
Anonymous has created a hyper cyber virus, which steals data from the CIA. 
The virus is known for its innovative and unbelievably clever merging and 
dividing data into partitions. As the lead security developer in the CIA, 
you have been tasked to analyze the software of the virus and observe its actions on the data. 
You will receive a single input line containing strings, separated by spaces. 
The strings may contain any ASCII character except whitespace. 
Then you will begin receiving commands in one of the following formats:
•	merge {startIndex} {endIndex}
•	divide {index} {partitions}
Every time you receive the merge command, you must merge all elements from 
the startIndex to the endIndex. In other words, you should concatenate them. 
Example: {abc, def, ghi} -> merge 0 1 -> {abcdef, ghi}
If any of the given indexes is out of the array, you must take only the range 
that is inside the array and merge it.
Every time you receive the divide command, you must divide the element at the 
given index into several small substrings with equal length. 
The count of the substrings should be equal to the given partitions. 
Example: {abcdef, ghi, jkl} -> divide 0 3 -> {ab, cd, ef, ghi, jkl}
If the string cannot be exactly divided into the given partitions, 
make all partitions except the last with equal lengths and make the last one - the longest. 
Example: {abcd, efgh, ijkl} -> divide 0 3 -> {a, b, cd, efgh, ijkl}
The input ends when you receive the command "3:1". At that point, 
you must print the resulting elements, joined by a space.
Input
•	The first input line will contain the array of data.
•	On the next several input lines, you will receive commands in the format specified above.
•	The input ends when you receive the command "3:1".
Output
•	As output, you must print a single line containing the elements of the array, joined by a space.
Constrains
•	The strings in the array may contain any ASCII character except whitespace.
•	The startIndex and the endIndex will be in the range [-1000…1000].
•	The endIndex will always be greater than the startIndex.
•	The index in the divide command will always be inside the array.
•	The partitions will be in the range [0…100].
•	Allowed working time/memory: 100ms / 16MB.


____________________________________________________________________________________________
Example_01

Input
Ivo Johny Tony Bony Mony
merge 0 3
merge 3 4
merge 0 3
3:1

Output
IvoJohnyTonyBonyMony


____________________________________________________________________________________________
Example_02

Input
abcd efgh ijkl mnop qrstuvwxyz
merge 4 10
divide 4 5
3:1

Output
abcd efgh ijkl mnop qr st uv wx yz

"""
