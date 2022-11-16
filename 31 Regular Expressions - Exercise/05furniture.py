import re


class Extract:
    def __init__(self, text):
        self.text = text

    def extracting(self):
        information = re.search(r'>{2}([A-Za-z]+)<{2}(\d+\.?[0-9]*)!(\d+)', self.text)
        if information:
            return information.groups()
        return None


bought_furniture = []
total_price = 0

while True:
    command = input()
    if command == 'Purchase':
        break

    result = Extract(command)
    if result.extracting() is not None:
        furniture = result.extracting()[0]
        single_price = float(result.extracting()[1])
        quantity = int(result.extracting()[2])
        bought_furniture.append(furniture)
        total_price += quantity * single_price

print('Bought furniture:')
for product in bought_furniture:
    print(product)
print(f'Total money spend: {total_price:.2f}')

#################################### TASK CONDITION ############################
"""

                                 5.	Furniture
Write a program that calculates the total cost of bought furniture. 
You will be given information about each purchase on separate lines until you receive 
the command "Purchase". Valid information should be in the format:
">>{furniture_name}<<{price}!{quantity}".
The price could be a floating-point or integer number. 
You should store the names of the furniture and the total price. 
In the end, print the name of each bought furniture and the total cost, 
formatted to the second decimal point:
"Bought furniture:
{1st name}
{2nd name}
…
{N name}
Total money spend: {total_cost}"

____________________________________________________________________________________________
Example

Input
>>Sofa<<312.23!3
>>TV<<300!5
>Invalid<<!5
Purchase	

Output
Bought furniture:
Sofa
TV
Total money spend: 2436.69	

Explanation
Only the Sofa and the TV are valid, for each of them 
we multiply the price by the quantity and print the result

"""
