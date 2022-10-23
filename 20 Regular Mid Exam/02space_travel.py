rout = input().split('||')
fuel = int(input())
ammo = int(input())

for command in rout:
    if command == 'Titan':
        print("You have reached Titan, all passengers are safe.")
        break

    action, number = command.split()

    if action == 'Travel':
        distance = int(number)
        if fuel - distance < 0:
            print("Mission failed.")
            break
        else:
            fuel -= distance
            print(f"The spaceship travelled {distance} light-years.")
    elif action == 'Enemy':
        enemy_armor = int(number)
        if ammo - enemy_armor >= 0:
            ammo -= enemy_armor
            print(f"An enemy with {enemy_armor} armour is defeated.")
        else:
            escape_fuel = enemy_armor * 2
            if fuel - escape_fuel >= 0:
                fuel -= escape_fuel
                print(f"An enemy with {enemy_armor} armour is outmaneuvered.")
            else:
                print("Mission failed.")
                break
    elif action == 'Repair':
        refil_fuel = int(number)
        refil_ammo = int(number) * 2
        fuel += refil_fuel
        ammo += refil_ammo
        print(f"Ammunitions added: {refil_ammo}.")
        print(f"Fuel added: {refil_fuel}.")
