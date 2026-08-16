# this is how to ask what kind of car someone wants and respond to it
car = input("What kind of car would you like? ")
print(f"let me see if i can find you a {car.title()}.")

# this is how to use "int" to find a number and ask how many people are at your table tonight
party_size = input("How many people are in your party tonight ")
party_size = int(party_size)
if party_size > 8:
    print("I'm sorry, you will need to wait for a table.")
else:
    print("Perfect, right this way! Your table is ready!")

# finding multiples of 10
number = input("Give me a number, please: ")
number = int(number)
if number % 10 == 0:
    print(f"{number} is a multiple of 10")
else:
    print(f"{number} is not a multiple of 10")

# adding toppings to pizza and saying quit when finished

prompt = "\nWhat topping would you like on your pizza?"
prompt += "\nEnter 'quit' when you are finished: "

while True:
    topping = input(prompt)
    if topping != 'quit' :
        print(f"    I'll add {topping} to your pizza.")
    else:
        break

prompt = "\nWhat sport do you want to write about?"
prompt += "\nEnter 'quit' when you are done. "
while True:
    sport = input(prompt)
    if sport != 'quit' :
        print(f"    I will help you write about {sport}")
    else:
        break

# this is how to charge different amounts for different ages

prompt = "\nHow old are you?"
prompt += "\nEnter 'quit' when you are done. "
while True:
    age = input(prompt)
    if age == 'quit' :
        break
    age = int(age)

    if age < 3:
        print(" you get in free")
    elif age < 13:
        print(" your ticket is $10")
    else:
        print(" your ticket is $15")