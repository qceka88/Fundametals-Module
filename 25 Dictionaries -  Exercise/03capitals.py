countries = input().split(', ')
capitals = input().split(', ')
country_capital_dict = {countries[i]:capitals[i] for i in range(len(countries))}
print("\n".join(f'{country} -> {capital}' for country, capital in country_capital_dict.items()))





#################################### TASK CONDITION ############################
"""
                           3.	Capitals
Using a dictionary comprehension, write a program that receives country 
names on the first line, separated by comma and space ", ", and their 
corresponding capital cities on the second line (again separated by comma 
and space ", "). Print each country with their capital on a separate line 
in the following format: "{country} -> {capital}".
Hints
•	You could use the zip() method.


____________________________________________________________________________________________
Example_01

Input
Bulgaria, Romania, Germany, England
Sofia, Bucharest, Berlin, London

Output
Bulgaria -> Sofia
Romania -> Bucharest
Germany -> Berlin
England -> London


____________________________________________________________________________________________
Example_02

Input
Bulgaria, Germany, France
Varna, Frankfurt, Paris

Output
Bulgaria -> Varna
Germany -> Frankfurt
France -> Paris

"""
