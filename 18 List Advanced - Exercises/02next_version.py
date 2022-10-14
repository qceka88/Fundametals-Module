#################### variant 01 ################

old_version = input().replace('.', '')
new_version = int(old_version) + 1
print('.'.join(str(new_version)))

################### variant 02 ################

old_version = list(map(int, input().split('.')))
old_version[-1] += 1
for index in range(len(old_version) - 1, -1, -1):
    if old_version[index] > 9:
        old_version[index] = 0
        if index - 1 >= 0:
            old_version[index - 1] += 1


print(*old_version,sep='.')



#################################### TASK CONDITION ############################
"""
                2.	Next Version
You are fed up with changing the version of your software manually. 
Instead, you will create a little script that will make it for you.
You will be given a string representing the version of your software in 
the format: "{n1}.{n2}.{n3}". Your task is to print the next version. 
For example, if the current version is "1.3.4", the next version will be "1.3.5". 
The only rule is that the numbers cannot be greater than 9. 
If it happens, set the current number to 0 and increase the previous number. 
For more clarification, see the examples below. 
Note: there will be no case in which the first number will become greater than 9.


____________________________________________________________________________________________
Examples

Input   |   Outut
1.2.3   |   1.2.4
1.3.9   |   1.4.0
3.9.9   |   4.0.0

"""
