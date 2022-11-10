class Clear:

    def __init__(self, first, second):
        self.first = first
        self.second = second

    def clear_word(self):
        while self.first in self.second:
            self.second = self.second.replace(self.first, '')
        return self.second

    def __repr__(self):
        return f'{self.clear_word()}'


first_string = input()
second_string = input()

clearing = Clear(first_string, second_string)
print(clearing)



#################################### TASK CONDITION ############################
"""
                                3.	Substring
On the first line, you will receive a string. On the second line, 
you will receive a second string. Write a program that removes all the 
occurrences of the first string in the second until there is no match. 
At the end, print the remaining string.


____________________________________________________________________________________________
Example_01

Input
ice

Output
kicegiciceeb

Explanation
kgb	We remove ice once and we get "kgiciceeb"
We match "ice" one more time and we get "kgiceb"
There is one more match. The finam result is "kgb"

"""
