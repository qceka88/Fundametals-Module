def even_extract(input_data):
    even_list = [number for number in input_data if number % 2 == 0]
    return even_list


def odd_extract(input_data):
    odd_list = [number for number in input_data if number % 2 != 0]
    return odd_list


def rightest_index(input_list, number):
    right_index = 0
    for indices, value in enumerate(input_list):
        if value == number and indices > right_index:
            right_index = indices
    return right_index


initial_list = list(map(int, input().split()))

while True:
    command = input().split()
    if 'end' in command:
        break
    order = command[0]
    if order == 'exchange':
        index = int(command[1])
        if len(initial_list) > index >= 0:
            left_part = initial_list[index + 1:]
            right_part = initial_list[:index + 1]
            initial_list = left_part + right_part
        else:
            print('Invalid index')
    elif order == 'max':
        type_of_number = command[1]
        if type_of_number == 'odd':
            odd_numbers = odd_extract(initial_list)
            if len(odd_numbers) == 0:
                print('No matches')
            else:
                max_odd = max(odd_numbers)
                index = rightest_index(initial_list, max_odd)
                print(index)
        elif type_of_number == 'even':
            even_numbers = even_extract(initial_list)
            if len(even_numbers) == 0:
                print('No matches')
            else:
                max_even = max(even_numbers)
                index = rightest_index(initial_list, max_even)
                print(index)
    elif order == 'min':
        type_of_number = command[1]
        if type_of_number == 'odd':
            odd_numbers = odd_extract(initial_list)
            if len(odd_numbers) == 0:
                print('No matches')
            else:
                min_odd = min(odd_numbers)
                index = rightest_index(initial_list, min_odd)
                print(index)
        elif type_of_number == 'even':
            even_numbers = even_extract(initial_list)
            if len(even_numbers) == 0:
                print('No matches')
            else:
                min_even = min(even_numbers)
                index = rightest_index(initial_list, min_even)
                print(index)
    elif order == 'first':
        count = int(command[1])
        if count > len(initial_list):
            print('Invalid count')
        else:
            type_of_number = command[2]
            if type_of_number == 'even':
                even_numbers = even_extract(initial_list)
                print(even_numbers[:count])
            elif type_of_number == 'odd':
                odd_numbers = odd_extract(initial_list)
                print(odd_numbers[:count])
    elif order == 'last':
        count = int(command[1])
        if count > len(initial_list):
            print('Invalid count')
        else:
            type_of_number = command[2]
            if type_of_number == 'even':
                even_numbers = even_extract(initial_list)
                print(even_numbers[-count:])
            elif type_of_number == 'odd':
                odd_numbers = odd_extract(initial_list)
                print(odd_numbers[-count:])

print(initial_list)

#################################### TASK CONDITION ############################
"""
                           6.	List Manipulator
Trifon has finally become a junior developer and has received his first task. 
It is about manipulating a list of integers. He is not quite happy about it 
since he hates manipulating lists. They will pay him a lot of money, though, 
and he is willing to give somebody half of it if to help him do his job. On the other hand,
you love lists (and money), so you decide to try your luck.
The list may be manipulated by one of the following commands:
•	"exchange {index}" – splits the list after the given index and exchanges the 
places of the two resulting sub-lists. E.g., [1, 2, 3, 4, 5] -> "exchange 2" -> result: [4, 5, 1, 2, 3]
o	If the index is outside the boundaries of the list, print "Invalid index"
o	A negative index is considered invalid
•	"max even/odd"– returns the INDEX of the max even/odd element.
 E.g., [1, 4, 8, 2, 3] -> "max odd" -> print: 4
•	"min even/odd" – returns the INDEX of the min even/odd element. 
E.g. [1, 4, 8, 2, 3] -> "min even" -> print: 3
o	If there are two or more equal min/max elements, return the index of the rightmost one
o	If a min/max even/odd element cannot be found, print "No matches"
•	"first {count} even/odd" – returns the first count even/odd elements. 
E.g. [1, 8, 2, 3] -> "first 2 even" -> print [8, 2]
•	"last {count} even/odd" – returns the last count even/odd elements. 
E.g. [1, 8, 2, 3] -> "last 2 odd" -> print [1, 3]
o	If the count is greater than the list length, print "Invalid count"
o	If there are not enough elements to satisfy the count, print as many as you can.
 If there are zero even/odd elements, print an empty list "[]"
•	"end" - stop taking input and print the final state of the list
Input
•	The input data should be read from the console.
•	On the first line, the initial list is received as a line of integers, separated by a single space.
•	On the following lines, until the command "end" is received, you will receive the list manipulation commands.
•	The input data will always be valid and in the format described. There is no need to check it explicitly.
Output
•	The output should be printed on the console.
•	On a separate line, print the output of the corresponding command.
•	On the last line, print the final list in square brackets with its elements separated by a comma and a space.
•	See the examples below to get a better understanding of your task.
Constraints
•	The number of input lines will be in the range [2 … 50].
•	The list elements will be integers in the range [0 … 1000].
•	The number of elements will be in the range [1 .. 50].
•	The split index will be an integer in the range [-231 … 231 – 1].
•	The first/last count will be an integer in the range [1 … 231 – 1].
•	There will not be redundant whitespace anywhere in the input.
•	Allowed working time for your program: 0.1 seconds. Allowed memory: 16 MB.


____________________________________________________________________________________________
Example_01

Input
1 3 5 7 9
exchange 1
max odd
min even
first 2 odd
last 2 even
exchange 3
end	

Output
2
No matches
[5, 7]
[]
[3, 5, 7, 9, 1]


____________________________________________________________________________________________
Example_02

Input
1 10 100 1000
max even
first 5 even
exchange 10
min odd
exchange 0
max even
min even
end	

Output
3
Invalid count
Invalid index
0
2
0
[10, 100, 1000, 1]


____________________________________________________________________________________________
Example_03

Input
1 10 100 1000
exchange 3
first 2 odd
last 4 odd
end

Output
[1]
[1]
[1, 10, 100, 1000]

"""
