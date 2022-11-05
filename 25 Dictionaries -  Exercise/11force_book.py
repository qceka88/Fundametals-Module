force_book = {}

while True:
    command = input()
    if command == 'Lumpawaroo':
        break

    if '|' in command:
        force_side, force_user = command.split(' | ')
        if force_side not in force_book.keys():
            force_book[force_side] = []
        not_in_book = True
        for side, users in force_book.items():
            if force_user in users:
                not_in_book = False
        if not_in_book:
            force_book[force_side].append(force_user)
    elif '->' in command:
        force_user, force_side = command.split(' -> ')
        if force_side not in force_book.keys():
            force_book[force_side] = []
        not_in_book = True
        for side, users in force_book.items():
            if force_user in users:
                not_in_book = False
        if not_in_book:
            force_book[force_side].append(force_user)
        elif not not_in_book:
            for side, users in force_book.items():
                if force_user in users:
                    force_book[side].remove(force_user)
            force_book[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")

for side, members in force_book.items():
    if len(members) > 0:
        print(f"Side: {side}, Members: {len(members)}")
        print('\n'.join(f'! {jedy}' for jedy in members))




#################################### TASK CONDITION ############################
"""
                               11.	*Force Book
The force users struggle to remember which side is the different force 
users from because they switch them too often. So you are tasked to create 
a web application to manage their profiles. You should store information for 
every unique force user registered in the application.
You will receive several input lines in one of the following formats:
"{force_side} | {force_user}"
"{force_user} -> {force_side}"
The "force_user" and "force_side" are strings, containing any character. 
If you receive "force_side | force_user":
•	If there is no such force user and no such force side -> create a new 
force side and add the force user to the corresponding side.
•	Only if there is no such force user in any force side -> add the force 
user to the corresponding side. 
•	If there is such force user already -> skip the command and continue to the next operation.
If you receive a "force_user -> force_side":
•	If there is such force user already -> change their side. 
•	If there is no such force user in any force side -> add the force user to 
the corresponding force side.
•	If there is no such force user and no such force side -> create new force 
side and add the force user to the corresponding side.
•	Then you should print on the console: "{force_user} joins the {force_side} side!".
You should end your program when you receive the command "Lumpawaroo". At that point, 
you should print each force side. For each side, print the force users.
In case there are no force users on a side, you shouldn't print the side information. 
Input / Constraints
•	The input comes in the form of commands in one of the formats specified above.
•	The input ends when you receive the command "Lumpawaroo".
Output
•	As output for each force side, you must print all the force users.
•	The output format is:
"Side: {force_side}, Members: {force_users_count}
! {force_user1}
! {force_user2}
…
! {force_userN}"
•	In case there are NO force users on a side, don't print this side. 


____________________________________________________________________________________________
Example_01

Input
Light | Peter
Dark | Kim
Light | Kim
Lumpawaroo

Output
Side: Light, Members: 1
! Peter
Side: Dark, Members: 1
! Kim

Explanation
We register Peter on the Light side and Kim on the Dark side. 
After receiving "Lumpawaroo", we print both sides.


____________________________________________________________________________________________
Example_02

Input
Lighter | Royal
Darker | DCay
Ivan Ivanov -> Lighter
DCay -> Lighter
Lumpawaroo

Output
Ivan Ivanov joins the Lighter side!
DCay joins the Lighter side!
Side: Lighter, Members: 3
! Royal
! Ivan Ivanov
! DCay

Explanation
Although Ivan Ivanov doesn't have a profile, we register him and add him to the Lighter side.
We remove DCay from the Darker side and add him to the Lighter side.
We print only the Lighter side because the Darker side has no members.

"""
