##################################### variant 01 #####################################

import re

input_line = input()
pattern = r'(\@|\#)([A-Za-z]{3,})\1\1([A-Za-z]{3,})\1'

match_pairs = re.findall(pattern, input_line)
mirror_words = [(pair[1], pair[2]) for pair in match_pairs if pair[1] == pair[2][::-1]]

if len(match_pairs) > 0:
    print(f'{len(match_pairs)} word pairs found!')
    if len(mirror_words) > 0:
        print('The mirror words are:')
        print(", ".join(f'{mirror[0]} <=> {mirror[1]}' for mirror in mirror_words))
    else:
        print("No mirror words!")
else:
    print("No word pairs found!")
    print("No mirror words!")

##################################### variant 02 #####################################

import re


class Regex:
    def __init__(self, some_pattern, some_data):
        self.some_pattern = some_pattern
        self.some_data = some_data

    def regex_action(self):
        match_pairs = re.findall(self.some_pattern, self.some_data)
        if match_pairs:
            return match_pairs
        return False


class Collect:
    __magic = r'(\@|\#)([A-Za-z]{3,})\1\1([A-Za-z]{3,})\1'

    def __init__(self, data):
        self.data = data

    def pairs_founder(self):
        pair_object = Regex(Collect.__magic, self.data).regex_action()
        if pair_object is not False:
            pairs = [(match[1], match[2]) for match in pair_object]
            if len(pairs) > 0:
                return pairs
        return False

    def mirrors_counter(self):
        if self.pairs_founder() is not False:
            mirror_words = [(pair[0], pair[1]) for pair in self.pairs_founder() if pair[0] == pair[1][::-1]]
            if len(mirror_words) > 0:
                return mirror_words
        return False

    def return_to_main(self):
        return self.pairs_founder(), self.mirrors_counter()


class Main:

    def __init__(self):
        self.some_input = input()
        self.pairs = []
        self.mirrors = []

    def collect_data(self):
        collected_data = Collect(self.some_input).return_to_main()
        self.pairs = collected_data[0]
        self.mirrors = collected_data[1]

    def printing(self):
        if self.pairs is not False:
            print(f'{len(self.pairs)} word pairs found!')
            if self.mirrors is not False:
                print('The mirror words are:')
                print(", ".join(f'{mirror[0]} <=> {mirror[1]}' for mirror in self.mirrors))
            else:
                print("No mirror words!")
        else:
            print("No word pairs found!")
            print("No mirror words!")


output = Main()
output.collect_data()
output.printing()


#################################### TASK CONDITION ############################
"""
                           Problem 2 - Mirror words
Problem for exam preparation for the Programming Fundamentals Course @SoftUni.
Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2307#1.

The SoftUni Spelling Bee competition is here. But it`s not like any other 
Spelling Bee competition out there. It`s different and a lot more fun! You, 
of course, are a participant, and you are eager to show the competition that 
you are the best, so go ahead, learn the rules and win!
On the first line of the input, you will be given a text string. 
To win the competition, you have to find all hidden word pairs, read them, 
and mark the ones that are mirror images of each other.
First of all, you have to extract the hidden word pairs. Hidden word pairs are:
•	Surrounded by "@" or "#" (only one of the two) in the following 
pattern #wordOne##wordTwo# or @wordOne@@wordTwo@
•	At least 3 characters long each (without the surrounding symbols)
•	Made up of letters only
If the second word, spelled backward, is the same as the first word and 
vice versa (casing matters!), they are a match, and you have to store them somewhere. 
Examples of mirror words: 
#Part##traP# @leveL@@Level@ #sAw##wAs#
•	If you don`t find any valid pairs, print: "No word pairs found!"
•	If you find valid pairs print their count: "{valid pairs count} word pairs found!"
•	If there are no mirror words, print: "No mirror words!"
•	If there are mirror words print:
"The mirror words are:
{wordOne} <=> {wordtwo}, {wordOne} <=> {wordtwo}, … {wordOne} <=> {wordtwo}"
Input / Constraints
•	You will recive a string.
Output
•	Print the proper output messages in the proper cases as described in the problem description.
•	If there are pairs of mirror words, print them in the end, each pair separated by ", ".
•	Each pair of mirror word must be printed with " <=> " between the words.

____________________________________________________________________________________________
Example_01

Input
@mix#tix3dj#poOl##loOp#wl@@bong&song%4very$long@thong#Part##traP##@@leveL@@Level@##car#rac##tu@pack@@ckap@#rr#sAw##wAs#r#@w1r

Output
5 word pairs found!
The mirror words are:
Part <=> traP, leveL <=> Level, sAw <=> wAs

Explanation
There are 5 green and yellow pairs that meet all 
requirements and thus are valid. 
#poOl##loOp# is valid and looks very much like a 
mirror words pair, but it isn`t because the casings don`t match.
#car#rac# "rac" spelled backward is "car", but this 
is not a valid pair because there is only one "#" between the words.
@pack@@ckap@ is also valid, but "ckap" backward 
is "pakc" which is not the same as "pack", so they are not mirror words.

____________________________________________________________________________________________
Example_02

Input
#po0l##l0op# @bAc##cAB@ @LM@ML@ #xxxXxx##xxxXxx# @aba@@ababa@

Output
2 word pairs found!
No mirror words!

Explanation
"xxxXxx" backward is not the same as "xxxXxx"
@aba@@ababa@ is a valid pair, but the word 
lengths are different - these are definitely not mirror words

____________________________________________________________________________________________
Example_01

Input
#lol#lol# @#God@@doG@# #abC@@Cba# @Xyu@#uyX#

Output
No word pairs found!
No mirror words!

"""