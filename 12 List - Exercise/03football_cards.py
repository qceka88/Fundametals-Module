team_A = ['A-1', 'A-2', 'A-3', 'A-4', 'A-5', 'A-6', 'A-7', 'A-8', 'A-9', 'A-10', 'A-11']
team_B = ['B-1', 'B-2', 'B-3', 'B-4', 'B-5', 'B-6', 'B-7', 'B-8', 'B-9', 'B-10', 'B-11']

input_cards = input().split()
game_stop = False

for card in input_cards:
    if card in team_A:
        team_A.remove(card)
    elif card in team_B:
        team_B.remove(card)
    if len(team_A) < 7 or len(team_B) < 7:
        game_stop = True
        break

print(f"Team A - {len(team_A)}; Team B - {len(team_B)}")
if game_stop:
    print('Game was terminated')


#################################### TASK CONDITION ############################
"""
                     3.	Football Cards
Most football fans love it for the goals and excitement. 
Well, this problem does not. You are up to handle the referee's 
little notebook and count the players who were sent off for fouls and misbehavior.
The rules: Two teams, named "A" and "B" have 11 players each. 
The players on each team are numbered from 1 to 11. 
Any player may be sent off the field by being given a red card.
 If one of the teams has less than 7 players remaining, the referee stops the game immediately,
  and the team with less than 7 players loses.
The card is a string with the team's letter ("A" or "B") followed by a single 
dash and the player's number. e.g., the card "B-7" means player #7 from team B received a card.
The task: You will be given a sequence of cards (could be empty), separated by a single space.

 You should print the count of remaining players on each team at the end of the game in the format: 
 "Team A - {players_count}; Team B - {players_count}". 
 If the referee terminated the game, print an additional line: "Game was terminated".
Note for the random tests: If a player who has already been sent off receives another card - ignore it.


____________________________________________________________________________________________
Example_01

Input
A-1 A-5 A-10 B-2

Output
Team A - 8; Team B - 10


____________________________________________________________________________________________
Example_02

Input
A-1 A-5 A-10 B-2 A-10 A-7 A-3

Output
Team A - 6; Team B - 10
Game was terminated

"""
