############################## variant 01 ############################
import re

input_text = input()

pattern = r'#([\w+\s]+)#(\d{2}\/\d{2}\/\d{2})#(\d+)#|\|([\w+\s]+)\|(\d{2}\/\d{2}\/\d{2})\|(\d+)\|'
filtered_products = re.findall(pattern, input_text)
clear_list = []

for row in filtered_products:
    cleared = []
    for value in row:
        if value:
            cleared.append(value)
    clear_list.append(cleared)

total_calories = sum([int(calories[2]) for calories in clear_list])
days = total_calories // 2000
print(f"You have food to last you for: {days} days!")

if days > 0:
    for product in clear_list:
        print(f"Item: {product[0]}, Best before: {product[1]}, Nutrition: {product[2]}")

############################## variant 02 ############################
import re

input_text = input()

pattern = r'(?P<sep>#|\|)([A-z\s]+)(?P=sep)(\d{2}\/\d{2}\/\d{2})(?P=sep)(\d+)(?P=sep)'
filtered_products = re.findall(pattern, input_text)

total_calories = sum([int(calories[3]) for calories in filtered_products])
days = total_calories // 2000
print(f"You have food to last you for: {days} days!")

if days > 0:
    for product in filtered_products:
        print(f"Item: {product[1]}, Best before: {product[2]}, Nutrition: {product[3]}")


#################################### TASK CONDITION ############################
"""
                            Problem 2 - Ad Astra
Problem for exam preparation for the Programming Fundamentals Course @SoftUni.
Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2525#1.

You are an astronaut who just embarked on a mission across the solar system. 
Since you will be in space for a long time, you have packed a lot of food with you. 
Create a program, which helps you identify how much food you have left 
and gives you information about its expiration date.
On the first line of the input, you will be given a text string. 
You must extract the information about the food and calculate the total calories. 
First, you must extract the food info. It will always follow the same pattern rules:
•	It will be surrounded by "|" or "#" (only one of the two) in the following pattern: 
#{item name}#{expiration date}#{calories}#   or 
|{item name}|{expiration date}|{calories}|
•	The item name will contain only lowercase and uppercase letters and whitespace
•	The expiration date will always follow the pattern: "{day}/{month}/{year}", 
where the day, month, and year will be exactly two digits long
•	The calories will be an integer between 0-10000
Calculate the total calories of all food items and then determine 
how many days you can last with the food you have. Keep in mind that you need 2000kcal a day.
Input / Constraints
•	You will receive a single string
Output
•	First, print the number of days you will be able to last with the food you have:
"You have food to last you for: {days} days!"
•	The output for each food item should look like this:
"Item: {item name}, Best before: {expiration date}, Nutrition: {calories}"

____________________________________________________________________________________________
Example_01

Input
#Bread#19/03/21#4000#|Invalid|03/03.20||Apples|08/10/20|200||Carrots|06/08/20|500||Not right|6.8.20|5|

Output
You have food to last you for: 2 days!
Item: Bread, Best before: 19/03/21, Nutrition: 4000
Item: Apples, Best before: 08/10/20, Nutrition: 200
Item: Carrots, Best before: 06/08/20, Nutrition: 500

Explanation
We have a total of three matches – bread, apples, and carrots. 
The sum of their calories is 4700. 
Since you need 2000kcal a day, we divide 4700/2000, 
which means this food will last you for 2 days.
We print each item

____________________________________________________________________________________________
Example_02

Input
$$#@@%^&#Fish#24/12/20#8500#|#Incorrect#19.03.20#450|$5*(@!#Ice Cream#03/10/21#9000#^#@aswe|Milk|05/09/20|2000|

Output
You have food to last you for: 9 days!
Item: Fish, Best before: 24/12/20, Nutrition: 8500
Item: Ice Cream, Best before: 03/10/21, Nutrition: 9000
Item: Milk, Best before: 05/09/20, Nutrition: 2000

Explanation
We have three matches. The total calories are 8500 + 9000 + 2000 = 19500, 
which means you have food for a total of 9 days.

____________________________________________________________________________________________
Example_03

Input
Hello|#Invalid food#19/03/20#450|$5*(@
Output

Comments
You have food to last you for: 0 days!	We have no matches, which means we have no food.
The colored text is not a match since it doesn't have a # at the end.

"""