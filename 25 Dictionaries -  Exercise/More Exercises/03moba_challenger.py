def battle_game(dict_players, first, second):
    common = False
    if first not in dict_players or second not in dict_players:
        return dict_players
    first_maps = [mp for mp in dict_players[first].keys()]
    second_maps = [mp for mp in dict_players[second].keys()]
    for map01 in first_maps:
        for map02 in second_maps:
            if map01 == map02:
                common = True
                break
    if common:
        first_points = sum(dict_players[first].values())
        second_points = sum(dict_players[second].values())
        if first_points > second_points:
            del dict_players[second]
        elif second_points > first_points:
            del dict_players[first]
    return dict_players


players_dict = {}

while True:
    command = input()
    if command == 'Season end':
        break
    if '->' in command:
        name, zone, skill = command.split(' -> ')
        if name not in players_dict:
            players_dict[name] = {}
        if zone not in players_dict[name]:
            players_dict[name][zone] = 0
        if int(skill) > players_dict[name][zone]:
            players_dict[name][zone] = int(skill)
    elif 'vs' in command:
        player01, player02 = command.split(' vs ')
        players_dict = battle_game(players_dict, player01, player02)

for player, info in sorted(players_dict.items(), key=lambda x: (-(sum(x[1].values())), x[0])):
    total_skill = sum(info.values())
    print(f'{player}: {total_skill} skill')
    for zone_name, power in sorted(info.items(), key=lambda x: (-x[1], x[0])):
        print(f'- {zone_name} <::> {power}')




#################################### TASK CONDITION ############################
"""
                           3.	MOBA Challenger
You are a pro MOBA player, you are struggling to become а master of 
the Challenger tier. So, you carefully watch the statistics in the tier.
You will receive several input lines in one of the following formats:
"{player} -> {position} -> {skill}"
"{player} vs {player}"
The "player" and "position" are strings, and the given 
"skill" will be an integer number. You need to keep track of every player.
When you receive a player with his position and skill, add him to the 
players' pool, if he isn`t present, else add his position and skill or 
update his skill, only if the current position skill is lower than the new value.
If you receive "{player} vs {player}" and both players exist in the tier, 
they duel with the following rules:
•	If they got at least one position in common, the player with better total 
skill points wins and the other is demoted from the tier -> remove him. 
•	If they have same total skill points at the same positions, the duel is tie 
and they both continue in the Season.
•	If they don`t have positions in common, the duel isn`t happening and both continue in the Season.
You should end your program when you receive the command "Season end". 
At that point you should print the players, ordered by total skill in descending 
order, then ordered by player name in ascending order. For each player print their 
position and skill, ordered descending by skill, then ordered by position name in ascending order.
Input / Constraints
•	The input comes in the form of commands in one of the formats specified above.
•	Player and position will always be one word string, containing no whitespaces.
•	Skill will be an integer in the range [0, 1000].
•	There will be no invalid input lines.
•	The program ends when you receive the command "Season end".
Output
•	The output format for each player is:
"{player}: {total_skills} skill"
- {position1} <::> {skill}
- {position2} <::> {skill}
…
- {positionN} <::> {skill}"


____________________________________________________________________________________________
Example_01

Input
Peter -> Adc -> 400
George -> Jungle -> 300
Simon -> Mid -> 200
Simon -> Support -> 250
Season end

Output
Simon: 450 skill
- Support <::> 250
- Mid <::> 200
Peter: 400 skill
- Adc <::> 400
George: 300 skill
- Jungle <::> 300

Explanation
We order the players by total skill points descending, then by name. 
We print every position along its skill ordered descending by skill, then by position name.


____________________________________________________________________________________________
Example_02

Input
Peter -> Adc -> 400
Bush -> Tank -> 150
Frank -> Mid -> 200
Frank -> Support -> 250
Frank -> Tank -> 250
Peter vs Frank
Frank vs Bush
Frank vs Hide
Season end

Output
Frank: 700 skill
- Support <::> 250
- Tank <::> 250
- Mid <::> 200
Peter: 400 skill
- Adc <::> 400

Explanation
Frank and Peter don`t have common position, so the duel isn`t valid.
Frank wins vs Bush /common position: "Tank". Bush is demoted.
Hide doesn`t exist so the duel isn`t valid.
We print every player left in the tier.

"""
