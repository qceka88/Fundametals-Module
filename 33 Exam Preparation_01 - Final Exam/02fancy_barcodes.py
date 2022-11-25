#################################### variant 01 #####################################

import re

pattern = r'@#+([A-Z][A-Za-z0-9]{4,}[A-Z])@#+'

number_of_products = int(input())
for product in range(number_of_products):
    barcode = input()
    match_product = re.match(pattern, barcode)
    if match_product:
        match_group = re.findall(r'(\d)', match_product.group(1))
        if match_group:
            grup_number = ''.join(digit for digit in match_group)
            print(f'Product group: {grup_number}')
        else:
            print('Product group: 00')
    else:
        print('Invalid barcode')

##################################### variant 02 #####################################

import re


class Regex:
    """
     This class use input regex and input name to extract needed information
    """

    def __init__(self, some_pattern, some_input):
        self.some_pattern = some_pattern
        self.some_input = some_input

    def regex_action(self):
        match = re.findall(self.some_pattern, self.some_input)
        if match:
            return match
        return False


class Main:

    def __init__(self):
        self.quantity = int(input())
        self.log_file = []

    def reading_barcodes(self):
        for product in range(self.quantity):
            barcode = input()
            product_object = Regex(r'@#+([A-Z][A-Za-z0-9]{4,}[A-Z])@#+', barcode).regex_action()
            if product_object is not False:
                group_object = Regex(r'(\d)', *product_object).regex_action()
                if group_object:
                    group_number = ''.join(digit for digit in group_object)
                    self.log_file.append(f'Product group: {group_number}')
                else:
                    self.log_file.append('Product group: 00')
            else:
                self.log_file.append('Invalid barcode')

    def printing(self):
        print(*self.log_file, sep='\n')


output = Main()
output.reading_barcodes()
output.printing()

#################################### TASK CONDITION ############################
"""
                    Problem 2 - Fancy Barcodes
Problem for exam preparation for the Programming Fundamentals Course @SoftUni.
Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2303#1.

Your first task is to determine if the given sequence of 
characters is a valid barcode or not. 
Each line must not contain anything else but a valid barcode. A barcode is valid when:
•	It is surrounded by a "@" followed by one or more "#"
•	It is at least 6 characters long (without the surrounding "@" or "#")
•	It starts with a capital letter
•	It contains only letters (lower and upper case) and digits
•	It ends with a capital letter
Examples of valid barcodes: @###Che46sE@##, @#FreshFisH@#, @###Brea0D@###, @##Che46sE@##
Examples of invalid barcodes: ##InvaliDiteM##, @InvalidIteM@, @#Invalid_IteM@#
Next, you have to determine the product group of the item from the barcode. 
The product group is obtained by concatenating all the digits found in the barcode. 
If there are no digits present in the barcode, the default product group is "00".
Examples:  
@#FreshFisH@# -> product group: 00
@###Brea0D@### -> product group: 0
@##Che4s6E@## -> product group: 46
Input
On the first line, you will be given an integer n – the count of barcodes that you will be receiving next. 
On the following n lines, you will receive different strings.
Output
For each barcode that you process, you need to print a message.
If the barcode is invalid:
•	"Invalid barcode"
If the barcode is valid:
•	"Product group: {product group}"

____________________________________________________________________________________________
Example_01

Input
3
@#FreshFisH@#
@###Brea0D@###
@##Che4s6E@##

Output
Product group: 00
Product group: 0
Product group: 46

____________________________________________________________________________________________
Example_02

Input
6
@###Val1d1teM@###
@#ValidIteM@#
##InvaliDiteM##
@InvalidIteM@
@#Invalid_IteM@#
@#ValiditeM@#

Output
Product group: 11
Product group: 00
Invalid barcode
Invalid barcode
Invalid barcode
Product group: 00

"""
