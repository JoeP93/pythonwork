# inviting people to dinner from a list
dinner_invites = ['Brad Pitt', 'Liam Neeson', 'Leonardo DiCaprio']
length = len(dinner_invites)
message = f"Hello, {dinner_invites[0]} would you like to come to dinner this evening?"
print(message)
letter = f"Yo yo {dinner_invites[1]}, come to dinner tonight at my spot!"
print(letter)
invite = f"My mans {dinner_invites[2]}, you can't miss this dinner with the boys!"
print(invite)
print(dinner_invites[1])
print(message)
print(letter)
print(invite)
# adding invites at the beginning, in the middle, or to the end of the list.
new_guest = "Ben Affleck"
new_person = "Timmy Turner"
big_papa = "Ben Wallace"
dinner_invites.insert(0, new_guest)
dinner_invites.insert(3, new_person)
dinner_invites.append(big_papa)
mail = f"Get here asap {dinner_invites[3]}"
come_on = f"Can't miss this {dinner_invites[3]}"
last_melon = f"Last but not least {dinner_invites[-1]}, can you make it?"
print(message)
print(letter)
print(invite)
print(mail)
print(come_on)
print(last_melon)
print(dinner_invites)
uninvited = dinner_invites.pop(0) #removes ben affleck (how to pop items out of list but keep them for messages etc.)
message = f"Sorry {uninvited}, no room for you at the table anymore"
print(message)
print(dinner_invites)
uninvited = dinner_invites.pop(3)
message = f"Nope, {uninvited} can't make it either now."
print(message)
print(dinner_invites)
uninvited = dinner_invites.pop(1)
message = f"Stay away from here {uninvited}, we don't wanna see ya"
print(message)
print(dinner_invites)
uninvited = dinner_invites.pop(1)
message = f"No room for {uninvited} anymore either. sorry"
print(message)
print(dinner_invites)
# this is how to delete items from list
del dinner_invites[1]
del dinner_invites[0]
print(dinner_invites)
#this is how to say HOW MANY people are still in your list
message = f"there will be {length} people arriving at 6 o'clock"
print(message)