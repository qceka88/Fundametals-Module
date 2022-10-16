population = list(map(int, input().split(', ')))
wage = int(input())

not_fair = False

for index in range(len(population)):
    richie_rich = max(population)
    current_human = population[index]

    if current_human < wage:
        diff = wage - current_human
        richie_rich_index = population.index(richie_rich)
        population[index] += diff
        if population[richie_rich_index] - diff >= wage:
            population[richie_rich_index] -= diff
        else:
            not_fair = True

if not_fair:
    print('No equal distribution possible')
else:
    print(population)



#################################### TASK CONDITION ############################
"""
               1.	Social Distribution
A core idea of several left-wing ideologies is that the 
wealthiest should support the poorest, no matter what, 
and that is exactly what you are called to do for this problem.
On the first line, you will be given the population 
(numbers separated by comma and space ", "). On the second line, 
you will be given the minimum wealth. You should distribute the wealth so 
that no part of the population has less than the minimum wealth.
To do that, you should always take wealth from the wealthiest part of the population. 
There will be cases where the distribution will not be possible. 
In that case, print: "No equal distribution possible". 


____________________________________________________________________________________________
Example_01

Input
2, 3, 5, 15, 75
5

Output
[5, 5, 5, 15, 70]


____________________________________________________________________________________________
Example_02

Input
2, 3, 5, 15, 75
20

Output
[20, 20, 20, 20, 20]


____________________________________________________________________________________________
Example_03

Input
2, 3, 5, 45, 45
30

Output
No equal distribution possible

"""
