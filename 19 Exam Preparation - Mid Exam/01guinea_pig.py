food_in_grams = float(input()) * 1000
hay_in_grams = float(input()) * 1000
cover_in_grams = float(input()) * 1000
pig_weight_grams = float(input()) * 1000

enough_supply = True

for day in range(1, 31):
    food_in_grams -= 300
    if day % 2 == 0:
        given_hay = food_in_grams * 0.05
        hay_in_grams -= given_hay
    if day % 3 == 0:
        given_cover = pig_weight_grams / 3
        cover_in_grams -= given_cover

    if food_in_grams <= 0 or hay_in_grams <= 0 or cover_in_grams <= 0:
        print("Merry must go to the pet store!")
        enough_supply = False
        break

if enough_supply:
    food_kg = food_in_grams / 1000
    hay_kg = hay_in_grams / 1000
    cover_kg = cover_in_grams / 1000
    print(f"Everything is fine! Puppy is happy! Food: {food_kg:.2f}, Hay: {hay_kg:.2f}, Cover: {cover_kg:.2f}.")



#################################### TASK CONDITION ############################
"""
                                    1.	Guinea Pig
Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2031#0.

Merry has a guinea pig named Puppy, whom she loves very much. 
Every month she goes to the nearest pet store and buys him everything he needs – food, hay, and cover.
On the first three lines, you will receive the quantity of food, hay, and cover, 
which Merry buys for a month (30 days). On the fourth line, you will receive the guinea pig's weight.
Every day Puppy eats 300 gr of food. Every second day Merry first feeds the pet, 
then gives it a certain amount of hay equal to 5% of the rest of the food. 
On every third day, Merry puts Puppy cover with a quantity of 1/3 of its weight.
Calculate whether the quantity of food, hay, and cover, will be enough for a month.
If Merry runs out of food, hay, or cover, stop the program!
Input
•	On the first line – quantity food in kilograms - a floating-point number in the range [0.0 – 10000.0]
•	On the second line – quantity hay in kilograms - a floating-point number in the range [0.0 – 10000.0]
•	On the third line – quantity cover in kilograms - a floating-point number in the range [0.0 – 10000.0]
•	On the fourth line – guinea's weight in kilograms - a floating-point number in the range [0.0 – 10000.0]
Output
•	If the food, the hay, and the cover are enough, print:
o	"Everything is fine! Puppy is happy! Food: {excessFood}, Hay: {excessHay}, Cover: {excessCover}."
•	If one of the things is not enough, print:
o	"Merry must go to the pet store!"
The output values must be formatted to the second decimal place!


____________________________________________________________________________________________
Example_01

Input
10
5
5.2
1

Output
Everything is fine! Puppy is happy! Food: 1.00, Hay: 1.10, Cover: 1.87.


Explanation
You receive food – 10000, hay – 5000, cover – 5200, weight – 1000 (in grams). 
On the first day, Merry gives Puppy 300gr food – 9700gr food left.
On the second day, the food left is 9400gr, so the needed hay is 9400 * 5%  = 470, and the hay left is 4530. 
On the third day, the cover left is 4866.67, and the food left is 9100, and so on.
On the last day, Merry has: food – 1.00, hay – 1.10, and cover – 1.87.


____________________________________________________________________________________________
Example_02

Input
1
1.5
3
1.5

Output
Merry must go to the pet store!


____________________________________________________________________________________________
Example_03

Input
9
5
5.2
1

Output
Merry must go to the pet store!

"""
