class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammal = []
        self.fish = []
        self.bird = []

    def add_animal(self, species, name):
        if species == 'mammal':
            self.mammal.append(name)
        elif species == 'fish':
            self.fish.append(name)
        elif species == 'bird':
            self.bird.append(name)
        Zoo.__animals += 1

    def get_info(self, species):
        if species == 'mammal':
            return f"{species.capitalize()}s in {self.name}: {', '.join(self.mammal)}\nTotal animals: {Zoo.__animals}"
        elif species == 'fish':
            return f"{species.capitalize()}es in {self.name}: {', '.join(self.fish)}\nTotal animals: {Zoo.__animals}"
        elif species == 'bird':
            return f"{species.capitalize()}s in {self.name}: {', '.join(self.bird)}\nTotal animals: {Zoo.__animals}"


zoo_name = input()
animal_number = int(input())

zoo = Zoo(zoo_name)

for animal in range(animal_number):
    specie, type_of_animal = input().split()
    zoo.add_animal(specie, type_of_animal)

needed_specie = input()

print(zoo.get_info(needed_specie))

#################################### TASK CONDITION ############################
'''
                               4.	Zoo
Create a class Zoo. It should have a class attribute called __animals that 
stores the total count of the animals in the zoo. The __init__ method should 
only receive the name of the zoo. There you should also create 3 empty lists 
(mammals, fishes, birds). The class should also have 2 more methods:
•	add_animal(species, name) - based on the species, adds the name to the corresponding list
•	get_info(species) - based on the species returns a string in the following format: 
"{Species} in {zoo_name}: {names}
Total animals: {total_animals}" 
On the first line, you will receive the name of the zoo. On the second line, 
you will receive number n. On the following n lines you will receive animal info 
in the format: "{species} {name}". Add the animal to the zoo to the corresponding list. 
The species could be "mammal", "fish", or "bird". 
On the final line, you will receive a species. 
At the end, print the info for that species and the total count of animals in the zoo.

_____________________________________________
Example_01

Input
Great Zoo
5
mammal lion
mammal bear
fish salmon
bird owl
mammal tiger
mammal

Output
Mammals in Great Zoo: lion, bear, tiger
Total animals: 5

_____________________________________________
Example_02

Input
Blah
1
mammal bear
mammal

Output
Mammals in Blah: bear
Total animals: 1

'''
