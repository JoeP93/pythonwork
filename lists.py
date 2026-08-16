#[] makes a list
pool_cues = ['Meucci', 'Predator', 'Cuetec', 'Mezz']
# this is how we use capatilization with lists
print(pool_cues[1])
print(pool_cues[2].upper())
print(pool_cues[-1].lower())
# this is how we form a message using specifics in the list
message = f"My first pool cue was a {pool_cues[0].title()}"
print(message)
quote = f"I really don't like {pool_cues[2].title()} as a brand."
print(quote)
# you can add items to the end of a list with .append('')
pool_cues.append('Jacoby')
print(pool_cues)
# you can start with an empty list and add to the list with .append('') as well!
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)
# this is how you .insert(0, '') something into the list into a specific area using any number
pool_cues.insert(0, 'Schon')
print(pool_cues)
# you can delete items in the list with del and which value it's at
del motorcycles[0]
print(motorcycles)
broken_poolcues = pool_cues.pop()
print(broken_poolcues)
# to show the last item on the list you can use the pop method but it will no longer show in the list.
last_owned = pool_cues.pop()
print(f"The last pool cue I bought was a {last_owned.title()}.")
# if you want to delete an item and not use it again, use del. If you want to use an item as you remove it use pop.
