# creating a list, sorting the list and showing it didn't permanently change it
vacations = ['Cancun', 'Bali', 'Cabo', 'Hawaii', 'Maldives']
print(vacations)
print(sorted(vacations))
print(vacations)
#how to reverse a list in alphabetical order
reversed_list = sorted(vacations, reverse=True)
print(reversed_list) 
#reverse the list
vacations.reverse()
print(vacations)
vacations.reverse()
print(vacations)
# permanently sort list in ABC order
vacations.sort()
print(vacations)
# this is how to specify the length of the list above
length = len(vacations)
message = f"there is {length} places i would like to go this summer."
print(message)