class Decryption:

    def __init__(self, key, hidden_text):
        self.key = key
        self.hidden_text = hidden_text

    def new_message(self, symbol, index_of_key):
        letter = chr(ord(symbol) - self.key[index_of_key])
        return letter

    def decryption_of_text(self):
        index = 0
        unhidden_text = ''
        for character in self.hidden_text:
            new_letter = self.new_message(character, index)
            unhidden_text += new_letter
            index += 1
            if index == len(self.key):
                index = 0
        return unhidden_text

    def treasure(self):
        start = self.decryption_of_text().index('&')
        end = self.decryption_of_text().index('&', start + 1)
        treasure = self.decryption_of_text()[start + 1:end]
        return treasure

    def coordinates(self):
        start = self.decryption_of_text().index('<')
        end = self.decryption_of_text().index('>')
        coordinates = self.decryption_of_text()[start + 1:end]
        return coordinates

    def __repr__(self):
        treasure = self.treasure()
        coordinates = self.coordinates()
        return f"Found {treasure} at {coordinates}"


input_key = list(map(int, input().split()))

while True:
    command = input()
    if command == 'find':
        break
    message = command
    decrypted_message = Decryption(input_key, message)
    print(decrypted_message)

#################################### TASK CONDITION ############################
"""
                        3.	Treasure Finder
Write a program that decrypts a message by a given key and gathers information 
about hidden treasure type and its coordinates. On the first line, you will receive 
a key (sequence of numbers separated by a space). On the next few lines, you will
receive lines with strings until you get the command "find". 
You should loop through every string and decrease the ASCII code of each 
character with a corresponding number of the key sequence. You choose a key number 
from the sequence by just looping through it. If the length of the key sequence is 
less than the string sequence, you should continue looping from the beginning. 
For more clarification, see the example below. 
After decrypting the message, you will get a type of treasure and its coordinates. 
The type will be between the symbol "&", and the coordinates - between the symbols "<' and '>'. 
For each line print the type and the coordinates in the format "Found {type} at {coordinates}".


____________________________________________________________________________________________
Example

Input
1 2 1 3
ikegfp'jpne)bv=41P83X@
ujfufKt)Tkmyft'duEprsfjqbvfv=53V55XA
find

Output
Found gold at 10N70W
Found Silver at 32S43W

Explanation
We start looping through the first string and the key. 
When we reach the end of the key, we start looping from the 
beginning of the key, but we continue looping through the string. (until the string is over)
The first message is: "hidden&gold&at<10N70W>" so we print we found gold at the given coordinates
We do the same for the second string 
"thereIs&Silver&atCoordinates<32S43W>"(starting from the beginning of the key and the beginning of the string)

"""
