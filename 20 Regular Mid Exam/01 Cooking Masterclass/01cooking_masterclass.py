from math import ceil

budget = float(input())
students = int(input())
flour_price = float(input())
eggs_pack_price = float(input()) * 10
apron_price = float(input())

free_flour = 0
if students / 5 >= 1:
    free_flour = students // 5
total_flour_price = (students - free_flour) * flour_price
total_eggs_price = students * eggs_pack_price
totaL_apron_price = ceil(students * 1.20) * apron_price

total_price = total_flour_price + total_eggs_price + totaL_apron_price

if total_price <= budget:
    print(f"Items purchased for {total_price:.2f}$.")
else:
    needed_money= total_price - budget
    print(f"{needed_money:.2f}$ more needed.")