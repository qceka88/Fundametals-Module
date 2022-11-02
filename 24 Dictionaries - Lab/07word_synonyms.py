from collections import defaultdict

cycles = int(input())
collection = defaultdict(list)

for number in range(cycles):
    word = input()
    synonym = input()

    collection[word].append(synonym)

for word, synonym_list in collection.items():
    print(f'{word} - {", ".join(syn for syn in synonym_list)}')



#################################### TASK CONDITION ############################
"""
                                  7.	Word Synonyms
Write a program, which keeps a dictionary with synonyms. The key of the 
dictionary will be the word. The value will be a list of all the synonyms 
of that word. You will be given a number n – the count of the words. 
After each term, you will be given a synonym, so the count of lines you 
should read from the console is 2 * n. You will be receiving a word and a 
synonym each on a separate line like this:
•	{word}
•	{synonym}
If you get the same word twice, just add the new synonym to the list. 
Print the words in the following format:
{word} - {synonym1, synonym2 … synonymN}


____________________________________________________________________________________________
Example_01

Input
3
cute
adorable
cute
charming
smart
clever

Output
cute - adorable, charming
smart - clever


____________________________________________________________________________________________
Example_02

Input
2
task
problem
task
assignment

Output
task – problem, assignment

"""
