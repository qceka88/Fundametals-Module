class Emoticonator:

    def __init__(self, string):
        self.string = string

    def emoticon_finder(self):
        emojis = []
        for index in range(len(self.string)):
            if ':' == self.string[index]:
                emojis.append(f'{self.string[index]}{self.string[index + 1]}')
        return emojis

    def __repr__(self):
        return '\n'.join(emoji for emoji in self.emoticon_finder())


input_string = input()

emoticons = Emoticonator(input_string)

print(emoticons)





#################################### TASK CONDITION ############################
"""
                            5.	 Emoticon Finder
Find all emoticons in the text. An emoticon always starts with ":" and is followed by a symbol.
The input will be provided as a single string.


____________________________________________________________________________________________
Example

Input
There are so many emoticons nowadays :P. I have many ideas :O what input to place here :)

Output
:P
:O
:)

"""
