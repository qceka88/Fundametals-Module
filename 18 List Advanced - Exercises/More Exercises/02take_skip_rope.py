initital_string = input()

numbers_list = [int(symbol) for symbol in initital_string if symbol.isdigit()]
non_numbers = [symbol for symbol in initital_string if not symbol.isdigit()]
take_list = [take for index, take in enumerate(numbers_list) if index % 2 == 0]
skip_list = [skip for index, skip in enumerate(numbers_list) if index % 2 != 0]

new_string = ''

start = 0
end = 0

for index in range(len(take_list)):
    end += take_list[index]
    new_string += ''.join(non_numbers[start:end])
    start +=  skip_list[index] + take_list[index]
    end += skip_list[index]

print(new_string)



#################################### TASK CONDITION ############################
"""
                           2.	Take/Skip Rope
Write a program, which reads a string and skips through it, 
extracting a hidden message. The algorithm you should implement is as follows:
Let us take the string "skipTest_String044160" as an example.
Take every digit from the string and transfer it somewhere. 
After this operation, you should have two lists of items - a numbers list and a non-numbers list:
•	Numbers' list: [0, 4, 4, 1, 6, 0]
•	Non-numbers: [s, k, i, p, T, e, s, t, _, S, t, r, i, n, g]
After that, take every digit in the numbers list and split it up 
into a take list and a skip list. In the take list, 
you should keep all digits at an even index. In the skip list, 
you should keep all digits at an odd index.
•	Numbers' list: [0, 4, 4, 1, 6, 0]
•	Take list: [0, 4, 6]
•	Skip list: [4, 1, 0]
Afterward, iterate over both lists:
•	First, take m characters from the non-numbers list and store it in a result string
•	Then, skip n characters from the non-numbers list
Note that the skipped characters are summed up as they go. The process would look like this:
1.	Current string: "skipTest_String". Take 0 characters and skip 4 characters: 
•	Taken string: ""
•	Skipped string: "skip"
2.	The remaining string looks like this: "Test_String". Take 4 characters and skip 1 character:
•	Taken string: "Test"
•	Skipped string: "_"
3.	The string looks like this: "String". Take 6 characters and skip 0 characters:
•	Taken string: "String"
•	Skipped string: ""
4.	The final string is "TestString".
After that, print the final string on the console.
Constraints
•	The count of digits in the input string will always be even.
•	The encrypted message will contain any printable ASCII character.


____________________________________________________________________________________________
Example_01

Input
T2exs15ti23ng1_3cT1h3e0_Roppe

Output
TestingTheRope


____________________________________________________________________________________________
Example_02

Input
O{1ne1T2021wf312o13Th111xreve!!@!

Output
OneTwoThree!!!


____________________________________________________________________________________________
Example_03

Input
this forbidden mess of an age rating 0127504740

Output
hidden message

"""