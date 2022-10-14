##################### Variant 01 #######################

sentence = input().split()
new_list = [word for word in sentence if len(word) % 2 == 0]
print('\n'.join(word for word in new_list))

##################### Variant 02 #######################


print('\n'.join(word for word in input().split() if len(word) % 2 == 0))



#################################### TASK CONDITION ############################
"""
                      3.	Word Filter
Using comprehension, write a program that receives some text, 
separated by space, and take only those words whose length is even. 
Print each word on a new line.


____________________________________________________________________________________________
Examples_01

Input
kiwi orange banana apple

Output
kiwi
orange
banana


____________________________________________________________________________________________
Examples_02

Input
pizza cake pasta chips

Output
cake

"""
