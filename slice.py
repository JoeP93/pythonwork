# this is how to slice a list and change the end of the list to something different than the original
my_sports = ['baseball', 'basketball', 'football']
friend_sports = my_sports[:]
my_sports.append('pool')
friend_sports.append('hockey')
print("My favorite sports are:")
print(my_sports)
print("\nMy friends favorite sports are:")
print(friend_sports)
#this is how to make a loop to print out the sports in each list
for sport in my_sports:
    print(sport)
for sporty in friend_sports:
    print(sporty)