favorite_numbers = {
"JJ": 6,
"Promise": 11,
"Jaida": 100,
"Joe": 2
}

for name, number in favorite_numbers.items():
    print(f"Hey {name}, I heard your favorite number is {number}!\n")

#This is how to create a glossary/dictionary of information and print the values meanings

glossary = {
    'string': 'A series of characters treated as a single block of text.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in a particular order.',
    'loop': 'A block of code that repeats a number of times.',
    'dictionary': 'A collection of key-value pairs.',
    'Command': 'A word that creates an action.',
    'variable': 'a named reference or pointer that points to an object stored in the computers memory'
}

# printing what each word means in the glossary above without a message attached
word = 'string'
print(f"{word.title()}: {glossary[word]}\n")

word = 'comment'
print(f"{word.title()}: {glossary[word]}\n")

word = 'list'
print(f"{word.title()}: {glossary[word]}\n")

word = 'loop'
print(f"{word.title()}: {glossary[word]}\n")

word = 'dictionary'
print(f"{word.title()}: {glossary[word]}\n")

word = 'Command'
print(f"{word.title()}: {glossary[word]}\n")

for word, meaning in glossary.items():
    print(f"{word.title()} means {meaning.title()}.\n")

rivers = {
    'the amazon river': 'Columbia',
    'the nile river': 'Egypt',
    'the yangtze river': 'China'
}

for river, country in rivers.items():
    print(f"{river.title()} runs through {country.title()}!\n")

for river in rivers.keys():
    print(river.title())

for country in rivers.values():
    print(country.title())

# the base dictionary from the favorite_languages example
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

# list of people who took the poll
poll_list = ['jen', 'joe', 'sarah', 'jim', 'edward', 'phil']

for name in poll_list:
    # check if the person has already taken responded
    if name in favorite_languages.keys():
        print(f"Thank you for responding, {name.title()}\n")
    else:
        print(f"Hi {name.title()}, you are invited to take our favorite languages poll!\n")

people = {
    "Jabbott": {
        "first_name": "JJ",
        "last_name": "Abbott",
        "age": 31, 
        "city": "Kenmore",
},

    "JacobE": {
        "first_name": "Jacob",
        "last_name": "Engel",
        "age": 30,
        "city": "snohomish",
},

    "JasonC": {
        "first_name": "Jason",
        "last_name": "Castro",
        "age": 34,
        "city": "snohomish",
},

}

for person, info in people.items():
    print(f"\nUsername: {person}")
    full_name = f"{info['first_name']} {info['last_name']}"
    age_and_location = f"{info['age']} {info['city']}"
    print(f"\tFull name: {full_name.title()}")
    print(f"\tAge & Location: {age_and_location.title()}")

Dog_Owners = {
    'Jimmy': 'Poodle',
    'Carl': 'Retriever',
    'JJ': 'Chihuahua',
    'Joe': 'Husky',
    'Billy': 'Lab',
}
Pets = ['Poodle', 'Retriever', 'Chihuahua', 'Husky', 'Lab']
for person, pet in Dog_Owners.items():
    print(f"\n{person}'s dog is a {pet}\n")

    # Make an empty list to store the pets in.
pets = []

# Make individual pets, and store each one in the list.
pet = {
    'animal type': 'python',
    'name': 'john',
    'owner': 'guido',
    'weight': 43,
    'eats': 'bugs',
}
pets.append(pet)

pet = {
    'animal type': 'chicken',
    'name': 'clarence',
    'owner': 'tiffany',
    'weight': 2,
    'eats': 'seeds',
}
pets.append(pet)

pet = {
    'animal type': 'dog',
    'name': 'peso',
    'owner': 'eric',
    'weight': 37,
    'eats': 'shoes',
}
pets.append(pet)

# Display information about each pet.
for pet in pets:
    print(f"\nHere's what I know about {pet['name'].title()}:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")

favorite_places = {
    'eric': ['bear mountain', 'death valley', 'tierra del fuego'],
    'erin': ['hawaii', 'iceland'],
    'willie': ['mt. verstovia', 'the playground', 'new hampshire']
}

for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places to go are:")
    for place in places:
        print(f"- {place.title()}\n")

favorite_numbers = {
    'mandy': [42, 17],
    'micah': [42, 39, 56],
    'gus': [7, 12],
    }
for name, numbers in favorite_numbers.items():
    print(f"{name.title()} like the following numers:")
    for number in numbers:
        print(f"    {number}")

cities = {
    'santiago': {
        'country': 'chile',
        'population': 6_310_000,
        'nearby mountains': 'andes',
        },
    'talkeetna': {
        'country': 'united states',
        'population': 876,
        'nearby mountains': 'alaska range',
        },
    'kathmandu': {
        'country': 'nepal',
        'population': 975_453,
        'nearby mountains': 'himilaya',
        }
    }

for city, city_info in cities.items():
    country = city_info ['country'].title()
    population = city_info ['population']
    mountains = city_info ['nearby mountains'].title()

    print(f"\n{city.title()} is in {country}")
    print(f"    It has a population of about {population}")
    print(f"    The {mountains} mounats are nearby!")