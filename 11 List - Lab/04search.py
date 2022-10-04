lines = int(input())
filter = input()
unfiltered_list = []
filtered_list = []

for string in range(lines):
    current_string = input()
    if filter in current_string:
        filtered_list.append(current_string)
    unfiltered_list.append(current_string)

print(unfiltered_list)
print(filtered_list)

#################################### TASK CONDITION ############################
"""
                             4.	Search
On the first line, you will receive a number n. On the second line, 
you will receive a word. On the following n lines, you will be given some strings.
You should add them to a list and print them. After that, you should filter out only 
the strings that include the given word and print that list too.


____________________________________________________________________________________________
Example_01

Input
3
SoftUni
I study at SoftUni
I walk to work
I learn Python at SoftUni

Output
["I study at SoftUni", "I walk to work", "I learn Python at SoftUni"]
["I study at SoftUni", "I learn Python at SoftUni"]


____________________________________________________________________________________________
Example_02

Input
4
tomatoes
I love tomatoes
I can eat tomatoes forever
I don't like apples
Yesterday I ate two tomatoes

Output
["I love tomatoes", "I can eat tomatoes forever", "I don't like apples", "Yesterday I ate two tomatoes"]
["I love tomatoes", "I can eat tomatoes forever", "Yesterday I ate two tomatoes"]

"""
