import re


class FindMatches:

    def __init__(self, text, word):
        self.text = text
        self.word = word

    def extract(self):
        match = re.findall(fr'\b{self.word}\b', self.text)
        return match

    def __repr__(self):
        number_occurrences = len(self.extract())
        return f'{number_occurrences}'


sentence = input().lower()
searched_word = input().lower()

occurrences = FindMatches(sentence, searched_word)
print(occurrences)

#################################### TASK CONDITION ############################
"""

                          3.	Find Occurrences of Word in Sentence
Write a program that finds how many times a word is used in a string. 
The output is a single number indicating the number of times the string contains the word.
Note that letter case does not matter – it is case-insensitive.

____________________________________________________________________________________________
Example_01

Input
The waterfall was so high, that the child couldn't see its peak.
the	

Output
2

____________________________________________________________________________________________
Example_02

Input
How do you plan on achieving that? How? How can you even think of that? 
how	

Output
3

____________________________________________________________________________________________
Example_03

Input
There was one. Therefore I bought it. I wouldn't buy it otherwise.
there

Output
1

"""
