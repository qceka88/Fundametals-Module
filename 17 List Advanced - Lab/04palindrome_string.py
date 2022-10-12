############################## variant 01 ########################

initial_string = input().split(' ')
searched_word = input()
palindrome = [word for word in initial_string if word == word[::-1]]
occurences = [ocur for ocur in palindrome if ocur == searched_word]
print(palindrome)
print(f"Found palindrome {len(occurences)} times")

############################## variant 02 ########################

initial_string = input().split(' ')
searched_word = input()
palindrome = []

for word in initial_string:
    if word == word[::-1]:
        palindrome.append(word)

occurences = [ocur for ocur in palindrome if ocur == searched_word]
print(palindrome)
print(f"Found palindrome {len(occurences)} times")



#################################### TASK CONDITION ############################
"""
4.	Palindrome Strings
On the first line, you will receive words separated by a single space. 
On the second line, you will receive a palindrome. 
First, you should print a list containing all the found palindromes in the sequence. 
Then, you should print the number of occurrences of the given 
palindrome in the format: "Found palindrome {number} times".


____________________________________________________________________________________________
Example_01

Input
wow father mom wow shirt stats
wow

Output
['wow', 'mom', 'wow', 'stats']
Found palindrome 2 times


____________________________________________________________________________________________
Example_02

Input
hey how you doin? lol
mom

Output
['lol']
Found palindrome 0 times

"""
