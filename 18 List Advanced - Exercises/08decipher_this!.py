message = input().split()

reveal = []

for word in message:
    number_as_string = ''
    current_word = []
    for symbol in word:
        if symbol.isdigit():
            number_as_string += symbol
        else:
            current_word.append(symbol)
    number_as_digits = int(number_as_string)
    current_word.insert(0, chr(number_as_digits))
    if len(current_word) > 2:
        current_word[1], current_word[-1] = current_word[-1], current_word[1]
    reveal.append(''.join(current_word))

print(*reveal)



#################################### TASK CONDITION ############################
"""
                     8.	Decipher This!
You are given a secret message you should decipher. 
To do that, you need to know that in each word:
•	the second and the last letter are switched (e.g., Holle means Hello)
•	the first letter is replaced by its character code (e.g., 72 means H)


____________________________________________________________________________________________
Example_01

Input
72olle 103doo 100ya

Output
Hello good day


____________________________________________________________________________________________
Example_02

Input
82yade 115te 103o

Output
Ready set go

"""
