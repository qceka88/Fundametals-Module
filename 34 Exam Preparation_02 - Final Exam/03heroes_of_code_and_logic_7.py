##################################### variant 01 #####################################
number_of_heroes = int(input())
hero_dict = {}

for hero in range(number_of_heroes):
    name, hp_points, mp_points = input().split()
    hero_dict[name] = {'hit': int(hp_points), 'mana': int(mp_points)}

while True:
    command = input().split(' - ')
    if command[0] == 'End':
        break
    action, hero_name = command[0], command[1]
    if action == 'CastSpell':
        required_mana, spell_name = int(command[2]), command[3]
        if required_mana > hero_dict[hero_name]['mana']:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")
        else:
            hero_dict[hero_name]['mana'] -= required_mana
            print(f"{hero_name} has successfully cast {spell_name} and now has {hero_dict[hero_name]['mana']} MP!")
    elif action == 'TakeDamage':
        damage, enemy = int(command[2]), command[3]
        if damage >= hero_dict[hero_name]['hit']:
            hero_dict.pop(hero_name)
            print(f"{hero_name} has been killed by {enemy}!")
        else:
            hero_dict[hero_name]['hit'] -= damage
            print(f"{hero_name} was hit for {damage} HP by {enemy} and now has {hero_dict[hero_name]['hit']} HP left!")
    elif action == 'Recharge':
        mana_potion = int(command[2])
        max_mana = 200

        if hero_dict[hero_name]['mana'] + mana_potion > max_mana:
            mana_potion = max_mana - hero_dict[hero_name]['mana']
            hero_dict[hero_name]['mana'] = max_mana
        else:
            hero_dict[hero_name]['mana'] += mana_potion
        print(f"{hero_name} recharged for {mana_potion} MP!")
    elif action == 'Heal':
        hit_potion = int(command[2])
        max_hit = 100
        if hero_dict[hero_name]['hit'] + hit_potion > max_hit:
            hit_potion = max_hit - hero_dict[hero_name]['hit']
            hero_dict[hero_name]['hit'] = max_hit
        else:
            hero_dict[hero_name]['hit'] += hit_potion
        print(f"{hero_name} healed for {hit_potion} HP!")

for name_hero, data in hero_dict.items():
    print(name_hero)
    print(f'  HP: {data["hit"]}')
    print(f'  MP: {data["mana"]}')


##################################### variant 02 #####################################

class CastSpell:

    def __init__(self, some_dict, data):
        self.some_dict = some_dict
        self.data = data

    def casting(self):
        hero_name, required_mana, spell_name = self.data[1], int(self.data[2]), self.data[3]
        if required_mana > self.some_dict[hero_name]['mana']:
            return f"{hero_name} does not have enough MP to cast {spell_name}!"
        else:
            self.some_dict[hero_name]['mana'] -= required_mana
            left_mana = self.some_dict[hero_name]['mana']
            return f"{hero_name} has successfully cast {spell_name} and now has {left_mana} MP!"

    def return_to_game(self):
        return self.casting(), self.some_dict


class TakeDamage:

    def __init__(self, some_dict, data):
        self.some_dict = some_dict
        self.data = data

    def atacking(self):
        hero_name, damage, enemy = self.data[1], int(self.data[2]), self.data[3]
        if damage >= self.some_dict[hero_name]['hit']:
            self.some_dict.pop(hero_name)
            return f"{hero_name} has been killed by {enemy}!"
        else:
            self.some_dict[hero_name]['hit'] -= damage
            left_hp = self.some_dict[hero_name]['hit']
            return f"{hero_name} was hit for {damage} HP by {enemy} and now has {left_hp} HP left!"

    def return_to_game(self):
        return self.atacking(), self.some_dict


class Recharge:

    def __init__(self, some_dict, data):
        self.some_dict = some_dict
        self.data = data

    def recharging(self):
        hero_name, mana_potion = self.data[1], int(self.data[2])
        max_mana = 200

        if self.some_dict[hero_name]['mana'] + mana_potion > max_mana:
            mana_potion = max_mana - self.some_dict[hero_name]['mana']
            self.some_dict[hero_name]['mana'] = max_mana
        else:
            self.some_dict[hero_name]['mana'] += mana_potion
        return f"{hero_name} recharged for {mana_potion} MP!"

    def return_to_game(self):
        return self.recharging(), self.some_dict


class Heal:

    def __init__(self, some_dict, data):
        self.some_dict = some_dict
        self.data = data

    def healing(self):
        hero_name, hit_potion = self.data[1], int(self.data[2])
        max_hit = 100

        if self.some_dict[hero_name]['hit'] + hit_potion > max_hit:
            hit_potion = max_hit - self.some_dict[hero_name]['hit']
            self.some_dict[hero_name]['hit'] = max_hit
        else:
            self.some_dict[hero_name]['hit'] += hit_potion
        return f"{hero_name} healed for {hit_potion} HP!"

    def return_to_game(self):
        return self.healing(), self.some_dict


class Game:

    def __init__(self, some_dict, some_input):
        self.some_dict = some_dict
        self.some_input = some_input
        self.message = ''

    def define_actions(self):
        data = self.some_input.split(' - ')
        action = data[0]
        if action == 'CastSpell':
            cast_object = CastSpell(self.some_dict, data).return_to_game()
            self.message, self.some_dict = cast_object
        elif action == 'TakeDamage':
            damage_object = TakeDamage(self.some_dict, data).return_to_game()
            self.message, self.some_dict = damage_object
        elif action == 'Recharge':
            recharge_object = Recharge(self.some_dict, data).return_to_game()
            self.message, self.some_dict = recharge_object
        elif action == 'Heal':
            heal_object = Heal(self.some_dict, data).return_to_game()
            self.message, self.some_dict = heal_object

    def return_to_main(self):
        return self.message, self.some_dict


class Main:

    def __init__(self):
        self.hero_dict = {}
        self.number_of_heroes = int(input())
        self.log = []

    def fill_dict(self):
        for hero in range(self.number_of_heroes):
            name, hp_points, mp_points = input().split()
            self.hero_dict[name] = {'hit': int(hp_points), 'mana': int(mp_points)}

    def game_actions(self):
        while True:
            data = input()
            if data == 'End':
                break
            gaming = Game(self.hero_dict, data)
            gaming.define_actions()
            message, the_dict = gaming.return_to_main()
            self.log.append(message)
            self.hero_dict = the_dict

    def printing(self):
        print(*self.log, sep='\n')
        for name_hero, data in self.hero_dict.items():
            print(f'{name_hero}\n  HP: {data["hit"]}\n  MP: {data["mana"]}')


output = Main()
output.fill_dict()
output.game_actions()
output.printing()

#################################### TASK CONDITION ############################
"""
                    Problem 3 - Heroes of Code and Logic VII
Problem for exam preparation for the Programming Fundamentals Course @SoftUni.
Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2303#0.

You got your hands on the most recent update on the best MMORPG of all 
time – Heroes of Code and Logic. You want to play it all day long! 
So cancel all other arrangements and create your party!
On the first line of the standard input, you will receive an 
integer n – the number of heroes that you can choose for your party. 
On the next n lines, the heroes themselves will follow with their hit points 
and mana points separated by a single space in the following format: 
"{hero name} {HP} {MP}"
-	HP stands for hit points and MP for mana points
-	a hero can have a maximum of 100 HP and 200 MP
After you have successfully picked your heroes, you can start playing the game. 
You will be receiving different commands, each on a new line, separated by " – ", until the "End" command is given. 
There are several actions that the heroes can perform:
"CastSpell – {hero name} – {MP needed} – {spell name}"
•	If the hero has the required MP, he casts the spell, thus reducing his MP. Print this message: 
o	"{hero name} has successfully cast {spell name} and now has {mana points left} MP!"
•	If the hero is unable to cast the spell print:
o	"{hero name} does not have enough MP to cast {spell name}!"
"TakeDamage – {hero name} – {damage} – {attacker}"
•	Reduce the hero HP by the given damage amount. If the hero is still alive (his HP is greater than 0) print:
o	"{hero name} was hit for {damage} HP by {attacker} and now has {current HP} HP left!"
•	If the hero has died, remove him from your party and print:
o	"{hero name} has been killed by {attacker}!"
"Recharge – {hero name} – {amount}"
•	The hero increases his MP. If it brings the MP of the hero above the maximum value (200), 
MP is increased to 200. (the MP can't go over the maximum value).
•	 Print the following message:
o	"{hero name} recharged for {amount recovered} MP!"
"Heal – {hero name} – {amount}"
•	The hero increases his HP. If a command is given that would bring the HP of the 
hero above the maximum value (100), HP is increased to 100 (the HP can't go over the maximum value).
•	 Print the following message:
o	"{hero name} healed for {amount recovered} HP!"
Input
•	On the first line of the standard input, you will receive an integer n
•	On the following n lines, the heroes themselves will follow with their hit 
points and mana points separated by a space in the following format
•	You will be receiving different commands, each on a new line, separated by " – ", 
until the "End" command is given
Output
•	Print all members of your party who are still alive, in the following format 
(their HP/MP need to be indented 2 spaces):
"{hero name}
  HP: {current HP}
  MP: {current MP}"
Constraints
•	The starting HP/MP of the heroes will be valid, 32-bit integers will never be 
negative or exceed the respective limits.
•	The HP/MP amounts in the commands will never be negative.
•	The hero names in the commands will always be valid members of your party. 
No need to check that explicitly.

____________________________________________________________________________________________
Example_01

Input
2
Solmyr 85 120
Kyrre 99 50
Heal - Solmyr - 10
Recharge - Solmyr - 50
TakeDamage - Kyrre - 66 - Orc
CastSpell - Kyrre - 15 - ViewEarth
End

Output
Solmyr healed for 10 HP!
Solmyr recharged for 50 MP!
Kyrre was hit for 66 HP by Orc and now has 33 HP left!
Kyrre has successfully cast ViewEarth and now has 35 MP!
Solmyr
  HP: 95
  MP: 170
Kyrre
  HP: 33
  MP: 35

____________________________________________________________________________________________
Example_02

Input
4
Adela 90 150
SirMullich 70 40
Ivor 1 111
Tyris 94 61
Heal - SirMullich - 50
Recharge - Adela - 100
CastSpell - Tyris - 1000 - Fireball
TakeDamage - Tyris - 99 - Fireball
TakeDamage - Ivor - 3 - Mosquito
End

Output
SirMullich healed for 30 HP!
Adela recharged for 50 MP!
Tyris does not have enough MP to cast Fireball!
Tyris has been killed by Fireball!
Ivor has been killed by Mosquito!
Adela
  HP: 90
  MP: 200
SirMullich
  HP: 100
  MP: 40

Explanation
Heal – SirMullich healed for 30 HP due to the HP max limit.
Recharge – Adela recharged for 50 MP due to the MP max limit.
CastSpell – Tyris does not have enough MP to cast the spell.
TakeDamage – Tyris's HP is reduced by 99, thus becoming -5, which means he is dead.
TakeDamage – Ivor's HP is now -2, so he is dead too.
After the "End" command, we print the remaining living heroes.

"""
