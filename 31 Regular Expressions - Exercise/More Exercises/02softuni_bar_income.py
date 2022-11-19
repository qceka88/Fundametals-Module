################################# variant 01 #################################

import re

pattern = r'%([A-Z][a-z]+)%([^\|\$\%\.]*)<(\w+)>([^\|\$\%\.]*)\|(\d+)\|([^\|\$\%\.\d]*)(\d+(\.\d+)*)\$'


total_income = 0
while True:
    command = input()
    if command == 'end of shift':
        break
    match = re.search(pattern, command)
    if match:
        name = match.group(1)
        product = match.group(3)
        quantitiy = int(match.group(5))
        price = float(match.group(7))
        total_income += price * quantitiy
        print(f"{name}: {product} - {price * quantitiy:.2f}")


print(f"Total income: {total_income:.2f}")

################################# variant 02 #################################

import re


class Extract:

    def __init__(self, text):
        self.text = text
        self.pattern = r'%([A-Z][a-z]+)%([^\|\$\%\.]*)<(\w+)>([^\|\$\%\.]*)\|(\d+)\|([^\|\$\%\.\d]*)(\d+(\.\d+)*)\$'

    def regex_action_validation(self):
        match = re.search(self.pattern, self.text)
        if match:
            return match
        return None

    def name(self):
        current_name = self.regex_action_validation().group(1)
        return current_name

    def product(self):
        current_product = self.regex_action_validation().group(3)
        return current_product

    def current_price(self):
        current_quantity = int(self.regex_action_validation().group(5))
        current_price = float(self.regex_action_validation().group(7))
        total_price = current_price * current_quantity
        return total_price

    def printing(self):
        if self.regex_action_validation() is not None:
            name = self.name()
            product = self.product()
            price = self.current_price()
            print(f"{name}: {product} - {price:.2f}")


total_income = 0

while True:
    command = input()
    if command == 'end of shift':
        break
    softuni_bar = Extract(command)
    if softuni_bar.regex_action_validation() is not None:
        softuni_bar.printing()
        total_income += softuni_bar.current_price()

print(f"Total income: {total_income:.2f}")

#################################### TASK CONDITION ############################
"""
                    2.	SoftUni Bar Income
Let`s take a break and visit the game bar at SoftUni. It is about time for the
people behind the bar to go home and you are the person who has to draw the line and
calculate the money from the products that were sold throughout the day. Until you receive
a line with text "end of shift" you will be given lines of input. But before processing that
line you should do some validations first.

Each valid order should have a customer, product, count and a price:
•	Valid customer's name should be surrounded by '%' and must start 
with a capital letter, followed by lower-case letters
•	Valid product contains any word character (not only letters) 
and must be surrounded by '<' and '>' 
•	Valid count is an integer, surrounded by '|'
•	Valid price is any real number followed by '$'
The parts of a valid order should appear in the order given: customer, 
product, count and a price.Between each part there can be other symbols, 
except ('|', '$', '%' and '.') For each valid line print on the console: 
"{customerName}: {product} - {totalPrice}"
When you receive "end of shift" print the total amount of money for the day 
rounded to 2 decimal places in the following format: "Total income: {income}".
Input / Constraints
•	Strings that you have to process until you receive text "end of shift".
Output
•	Print all of the valid lines in the format "{customerName}: {product} - {totalPrice}"
•	After receiving "end of shift" print the total amount of money for the day rounded
to 2 decimal places in the following format: "Total income: {income}"
•	Allowed working time / memory: 100ms / 16MB.

____________________________________________________________________________________________
Example_01

Input
%George%<Croissant>|2|10.3$
%Peter%<Gum>|1|1.3$
%Maria%<Cola>|1|2.4$
end of shift	

Output
George: Croissant - 20.60
Peter: Gum - 1.30
Maria: Cola - 2.40
Total income: 24.30	

Explanation
Each line is valid, so we print each order, calculating the total price of the product bought.
At the end we print the total income for the day

____________________________________________________________________________________________
Example_02

Input
%InvalidName%<Croissant>|2|10.3$
%Peter%<Gum>1.3$
%Maria%<Cola>|1|2.4
%Valid%<Valid>valid|10|valid20$
end of shift	

Output
Valid: Valid - 200.00
Total income: 200.00	

Explanation
On the first line, the customer name isn`t valid, so we skip that line.
The second line is missing product count.
The third line don`t have a valid price.
And only the forth line is valid
"""
