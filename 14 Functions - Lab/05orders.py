def calculating(input_product, quantity_of_products):
    total_price = 0
    if input_product == 'coffee':
        total_price = quantity_of_products * 1.5
    elif input_product == 'water':
        total_price = quantity_of_products * 1
    elif input_product == 'coke':
        total_price = quantity_of_products * 1.4
    elif input_product == 'snacks':
        total_price = quantity_of_products * 2
    return total_price


product = input()
quantity = int(input())

price = calculating(product, quantity)
print(f'{price:.2f}')

#################################### TASK CONDITION ############################
"""
                            5.	Orders
Write a function that calculates the total price of an order and returns it. 
The function should receive one of the following products:
"coffee", "coke", "water", or "snacks", and a quantity of the product.

The prices for a single piece of each product are: 
•	coffee - 1.50
•	water - 1.00
•	coke - 1.40
•	snacks - 2.00

Print the result formatted to the second decimal place.


____________________________________________________________________________________________
Example_01

Input
water
5

Output
5.00


____________________________________________________________________________________________
Example_02

Input
coffee
2

Output
3.00

"""
