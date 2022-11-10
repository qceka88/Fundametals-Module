class Censorship:

    def __init__(self, words, text_content):
        self.words = words
        self.text_content = text_content

    def censoring(self):
        for word in self.words:
            while word in self.text_content:
                self.text_content = self.text_content.replace(word, '*' * len(word))
        return self.text_content

    def __repr__(self):
        return f'{self.censoring()}'


banned_words = input().split(', ')
text = input()

filtered = Censorship(banned_words, text)

print(filtered)




#################################### TASK CONDITION ############################
"""
                          4.	Text Filter
Write a program that receives a text and a string of banned words, 
separated by a comma and space ", ". All banned words in the text 
should be replaced with the number of asterisks "*", equal to the word's length. 
The ban list will be entered on the first input line and the text - on the second input line. 


____________________________________________________________________________________________
Example

Input
Linux, Windows
(Second part from input must be on single line!!!!)
It is not Linux, it is GNU/Linux. Linux is merely the kernel, while GNU adds the functionality. 
Therefore we owe it to them by calling the OS GNU/Linux! Sincerely, a Windows client

Output(on single line)
It is not *****, it is GNU/*****. ***** is merely the kernel, while GNU adds the functionality. 
Therefore we owe it to them by calling the OS GNU/*****! Sincerely, a ******* client


"""
