storage = {}

while True:
    command = input()
    if command == 'statistics':
        break

    product, quantity = command.split(': ')
    if product not in storage:
        storage[product] = 0
    storage[product] += int(quantity)

print("Products in stock:")
for product, quantity in storage.items():
    print(f'- {product}: {quantity}')

print(f'Total Products: {len(storage.keys())}')
print(f'Total Quantity: {sum(storage.values())}')



#################################### TASK CONDITION ############################
"""
                                3.	Statistics
You seem to be doing great at your first job, so your boss decides 
to give you as your next task something more challenging. You have 
to accept all the new products coming in the bakery and finally gather some statistics.
You will be receiving key-value pairs on separate lines separated 
by ": " until you receive the command "statistics". Sometimes you may 
receive a product more than once. In that case, you have to add the new 
quantity to the existing one. When you receive the "statistics" command, print the following:
"Products in stock:
- {product1}: {quantity1}
- {product2}: {quantity2}
…
- {productN}: {quantityN}
Total Products: {count_all_products}
Total Quantity: {sum_all_quantities}"


____________________________________________________________________________________________
Example_01

Input
bread: 4
cheese: 2
ham: 1
bread: 1
statistics

Output
Products in stock:
- bread: 5
- cheese: 2
- ham: 1
Total Products: 3
Total Quantity: 8


____________________________________________________________________________________________
Example_02

Input
eggs: 10
bread: 6
cheese: 8
milk: 7
statistics

Output
Products in stock:
- eggs: 10
- bread: 6
- cheese: 8
- milk: 7
Total Products: 4
Total Quantity: 31


"""
