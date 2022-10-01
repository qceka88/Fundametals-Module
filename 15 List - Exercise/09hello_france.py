colection_list = input().split('|')
budget = int(input())

ticket_to_france = 150
colected_money = []
for command in colection_list:
    input_command = command.split('->')
    item = input_command[0]
    price = float(input_command[1])

    if item == 'Clothes' and price <= 50:
        if budget - price >= 0:
            budget -= price
            sell_price = price * 1.40
            colected_money.append(sell_price)
    elif item == 'Shoes' and price <= 35:
        if budget - price >= 0:
            budget -= price
            sell_price = price * 1.40
            colected_money.append(sell_price)
    elif item == 'Accessories' and price <= 20.5:
        if budget - price >= 0:
            budget -= price
            sell_price = price * 1.40
            colected_money.append(sell_price)

profit = sum(colected_money) - (sum(colected_money) / 1.4)

print(*[f'{money:.2f}' for money in colected_money])
print(f"Profit: {profit:.2f}")
total_money = sum(colected_money) + budget
if total_money >= ticket_to_france:
    print('Hello, France!')
else:
    print('Not enough money.')


#################################### TASK CONDITION ############################
"""
                     9.	* Hello, France
You want to go to France by train, and the train ticket costs exactly 150$. 
You do not have enough money, so you decide to buy some items with your budget 
and then sell them at a higher price – with a 40% markup.
You will receive a collection of items and a budget in the following format:
{type->price|type->price|type->price……|type->price}
{budget}
The prices for each of the types cannot exceed a specific price, which is given below:
Type	Maximum Price
Clothes	50.00
Shoes	35.00
Accessories	20.50
If a price for a particular item is higher than the maximum price, don't buy it. 
Every time you buy an item, you have to reduce the budget with its price value. 
If you don't have enough money for it, you can't buy it. Buy as many items as you can.
Next, you should increase the price of each item you have successfully bought by 40% and then sell it. 
Calculate if the budget after selling all the items is enough for buying the train ticket.
Input / Constraints
•	On the 1st line, you will receive the items with their prices 
in the format described above – real numbers in the range [0.00……1000.00]
•	On the 2nd line, you are going to be given the budget – a real number in the range [0.0….1000.0]
Output
•	First, print the list with the bought item’s new prices, 
formatted to the second decimal point in the following format:
"{price1} {price2} {price3} … {priceN}"
•	Second, print the profit, formatted to the second decimal point in the following format:
"Profit: {profit}"
•	Finally:
o	If the budget is enough for buying the train ticket, print: "Hello, France!" 
o	Otherwise, print: "Not enough money."


____________________________________________________________________________________________
Example_01

Input
Clothes->43.30|Shoes->25.25|Clothes->36.52|Clothes->20.90|Accessories->15.60
120	

Output
60.62 35.35 51.13
Profit: 42.03
Hello, France!

Explanation
We start subtracting the valid prices from the budget:
120 – 43.40 = 76.7.
76.7 – 25.25 = 51.45
51.45 – 36.52 = 14.93
14.93 is less than 20.90 and 15.60, so we can't buy either of the last two. 
We must increase each price by 40%, and the new prices are 60.62 35.35 51.13. 
The profit is 42.03, and their new budget will be – 
what is left of the budget - 14.93 + {sum of all newPrices}. It is enough, so we print: Hello, France!


____________________________________________________________________________________________
Example_02

Input
Shoes->41.20|Clothes->20.30|Accessories->40|Shoes->15.60|Shoes->33.30|Clothes->48.60

Output
90	28.42 21.84 46.62
Profit: 27.68
Not enough money.

"""