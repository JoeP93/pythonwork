# making a list of sandiwich orders and printing that they are being made, and when they have been made
sandwich_orders = ['club', 'pastrami', 'italian', 'pastrami', 'ham', 'meatball', 'pastrami']
finished_sandwiches = []
# we are out of pastrami so it'll only print the sandwiches that able to be made at this time
print("\nI'm sorry we're all out of pastrami today.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print("\n")
while sandwich_orders:
    current_sandwiches = sandwich_orders.pop()
    print(f"I'm working on your {current_sandwiches} sandwich")
    finished_sandwiches.append(current_sandwiches)

print("\n")
for sandwich in finished_sandwiches:
    print(f"I made a {sandwich} sandwich.")

name_prompt = "\nWhat's your name? "
place_prompt = "If you could visit anywhere in the world, where would it be? "
continue_prompt = "\nWould you like anyone else to respond? (yes/no) "

responses = {}

while True:
    name = input(name_prompt)
    place = input (place_prompt)
    responses[name] = place
    repeat = input(continue_prompt)
    if repeat != 'yes':
        break

    print("\n--- RESULTS ---")
    for name, place in responses.items():
        print(f"{name.title()} would like to visit {place.title()}")