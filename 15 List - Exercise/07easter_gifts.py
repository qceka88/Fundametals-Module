gifts_list = input().split()

while True:
    command = input()
    if command == 'No Money':
        break
    input_data = command.split()
    order = input_data[0]
    gift = input_data[1]
    if order == 'OutOfStock':
        if gift in gifts_list:
            counter = gifts_list.count(gift)
            for count in range(counter):
                index = gifts_list.index(gift)
                gifts_list[index] = 'None'
    elif order == 'Required':
        index_of_gift = int(input_data[2])
        if index_of_gift >= 0 and index_of_gift < len(gifts_list):
            gifts_list[index_of_gift] = gift
    elif order == 'JustInCase':
        gifts_list[-1] = gift

for gift_name in gifts_list:
    if gift_name != 'None':
        print(gift_name, end=' ')


#################################### TASK CONDITION ############################
"""
                       7.	* Easter Gifts
As a good friend, you decide to buy presents for your friends.
Create a program that helps you plan the gifts for your friends and family. 
First, you are going to receive the gifts you plan on buying on a single line, 
separated by space, in the following format:
"{gift1} {gift2} {gift3}… {giftn}"
Then you will start receiving commands until you read the "No Money" message. 
There are three possible commands:
•	"OutOfStock {gift}"
o	Find the gifts with this name in your collection, if any, and change their values to "None".  
•	"Required {gift} {index}"
o	If the index is valid, replace the gift on the given index with the given gift. 
•	"JustInCase {gift}"
o	Replace the value of your last gift with this one. 
In the end, print the gifts on a single line, except the ones with value "None",
 separated by a single space in the following format:
"{gift1} {gift2} {gift3} … {giftn}"
Input / Constraints
•	On the 1st line,  you will receive the names of the gifts, separated by a single space.
•	On the following lines, until the "No Money" command is received, you will be receiving commands.
•	The input will always be valid.
Output
•	Print the gifts in the format described above.


____________________________________________________________________________________________
Example_01

Input
Eggs StuffedAnimal Cozonac Sweets EasterBunny Eggs Clothes
OutOfStock Eggs
Required Spoon 2
JustInCase ChocolateEgg
No Money

Output
StuffedAnimal Spoon Sweets EasterBunny ChocolateEgg

Explanation
First, we receive the command "OutOfStock", and we need to replace
 the values of "Eggs" with "None". After this command, the list should look like this: 
None StuffedAnimal Cozonac Sweets EasterBunny None Clothes
Afterward, we receive the "Required" command, and we need to replace the value
 on the 2nd index of our list with the value "Spoon". The list should look like this:  
None StuffedAnimal Spoon Sweets EasterBunny None Clothes
After, we receive the "JustInCase" command, which means we need to replace the 
last value in our list with "ChocolateEggs". The list should look like this:
None StuffedAnimal Spoon Sweets EasterBunny None ChocolateEggs 
In the end, we print all of the gifts, except the ones with values "None". 
The final list: StuffedAnimal Spoon Sweets EasterBunny ChocolateEggs 


____________________________________________________________________________________________
Example_02

Input
Sweets Cozonac Clothes Flowers Wine Clothes Eggs Clothes
Required Paper 8
OutOfStock Clothes
Required Chocolate 2
JustInCase Hat
OutOfStock Cable
No Money

Output
Sweets Cozonac Chocolate Flowers Wine Eggs Hat

"""
