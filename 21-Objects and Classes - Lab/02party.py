class Party:

    def __init__(self, people=[]):
        self.people = people

    def invited_people(self, human):
        self.people.append(human)

    def going_names(self):
        return f'Going: {", ".join(self.people)}'

    def quantity_people(self):
        return f"Total: {len(self.people)}"


party = Party()

while True:
    command = input()
    if command == 'End':
        break

    name = command
    party.invited_people(name)

print(party.going_names())
print(party.quantity_people())


#################################### TASK CONDITION ############################
'''
                          3.	Email
Create class Email. The __init__ method should receive sender, 
receiver and a content. It should also have a default set to 
False attribute called is_sent. The class should have two additional methods:
•	send() - sets the is_sent attribute to True
•	get_info() - returns the following string:
 "{sender} says to {receiver}: {content}. Sent: {is_sent}"
You will receive some information (separated by a single space) 
until you receive the command "Stop". The first element will be the sender, 
the second one – the receiver, and the third one – the content. 
On the final line, you will be given the indices of the sent emails separated by comma and space ", ". 
Call the send() method for the given indices of emails. For each email, call the get_info() method.
Note: submit all of your code, including the class


Example_01


Input
Peter John Hi,John
John Peter Hi,Peter!
Katy Lilly Hello,Lilly
Stop
0, 2	

Output
Peter says to John: Hi,John. Sent: True
John says to Peter: Hi,Peter!. Sent: False
Katy says to Lilly: Hello,Lilly. Sent: True
____________________________________________________
Example_01


Input
Anna, Bella, Hi
Sam, Dany, Okey
Felix, Mery, Bye
Stop
0	

Output
Anna, says to Bella,: Hi. Sent: True
Sam, says to Dany,: Okey. Sent: False
Felix, says to Mery,: Bye. Sent: False


'''
