class Validator:

    def __init__(self, ticket):
        self.ticket = ticket
        self.winning_symbols = ['@', '#', '$', '^']

    def validate_length(self):
        if len(self.ticket) != 20:
            return False
        return True

    def check_for_winning(self):
        wining = False
        left_part = self.ticket[:10]
        right_part = self.ticket[10:]
        for symbol in self.winning_symbols:
            for times in range(10, 5, -1):
                containing = times * symbol
                if containing in left_part and containing in right_part:
                    if times == 10:
                        return f'ticket "{self.ticket}" - {times}{symbol} Jackpot!'
                    return f'ticket "{self.ticket}" - {times}{symbol}'
        return wining

    def __repr__(self):
        if not self.validate_length():
            return "invalid ticket"
        elif not self.check_for_winning():
            return f'ticket "{self.ticket}" - no match'
        else:
            return f'{self.check_for_winning()}'


tickets = [ticket.strip() for ticket in input().split(', ')]

for current_ticket in tickets:
    winning = Validator(current_ticket)
    print(winning)






#################################### TASK CONDITION ############################
"""
                        10.	*Winning Ticket
The lottery is exciting. However, checking a million tickets for winnings 
only by hand is not. So, you are given the task of creating a program that 
automatically checks if a ticket is a winner.
You are given a collection of tickets separated by commas and spaces (one or many). 
You need to check each ticket to see if it has a winning combination of symbols:
•	A valid ticket has exactly 20 characters.
•	A winning ticket is a valid one, containing one of the symbols '@', '#', '$' or '^' 
uninterruptedly repeated at least 6 times in both halves of the tickets.
•	In order to win a Jackpot, the ticket should contain the same winning symbol 10 times on both sides
An example of a valid winning ticket:
"Cash$$$$$$Ca$$$$$$sh"
An example of a Jackpot winning valid ticket:
"$$$$$$$$$$$$$$$$$$$$"
Input
The input will be read from the console. The input consists of a single line containing 
all tickets separated by commas and one or more white spaces in the format:
•	"{ticket}, {ticket}, … {ticket}"
Output
Print the result for every ticket in the order of their appearance, each on a separate line in the format:
•	If the ticket is invalid: "invalid ticket"
•	If the ticket is valid, but it is not winning: "ticket "{ticket}" - no match"
•	If the ticket is valid and winning, but not a Jackpot: 
"ticket "{ticket}" - {uninterrupted_match_length}{match_symbol}"
•	It the ticket hits the Jackpot:
"ticket "{ticket}" - {uninterrupted_match_length}{match_symbol} Jackpot!"
Constrains
•	Number of tickets will be in range [0 … 100]


____________________________________________________________________________________________
Example_01

Input
Cash$$$$$$Ca$$$$$$sh

Output
ticket "Cash$$$$$$Ca$$$$$$sh" - 6$


____________________________________________________________________________________________
Example_02

Input
$$$$$$$$$$$$$$$$$$$$, aabb  , th@@@@@@eemo@@@@@@ey

Output
ticket "$$$$$$$$$$$$$$$$$$$$" - 10$ Jackpot!
invalid ticket
ticket "th@@@@@@eemo@@@@@@ey" - 6@

____________________________________________________________________________________________
Example_03

Input
validticketnomatch:(, Cas$$$$$$$Ca$$$$$$s$

Output
ticket "validticketnomatch:(" - no match
ticket "Cas$$$$$$$Ca$$$$$$s$" - 6$

"""
