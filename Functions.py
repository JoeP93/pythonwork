def display_message():
    """Display what is happening in this chapter"""
    msg = "I am learning about Functions."
    print(msg)

display_message()

def favorite_book(book):
    """Display my favorite book"""
    print(f"\nOne of my all time favorite books is {book.title()}!")

favorite_book('Alice In Wonderland')

def make_shirt(shirt_size, shirt_message):
    """Display information about a shirt."""
    print(f"\nThe size of the shirt is a {shirt_size}.")
    print(f"\nWith the message on the shirt being {shirt_message}.\n")
make_shirt('Large', 'YOLO')

def make_shirt(shirt_size, shirt_message):
    """Display information about a shirt."""
    print(f"\nThe size of the shirt is a {shirt_size}.")
    print(f"\nWith the message on the shirt being {shirt_message}.\n")
make_shirt(shirt_size='Large',shirt_message= 'YOLO')

def make_shirt(size, message):
    """Summarize the shirt that's going to be made."""
    print(f"\nI'm going to make a {size} t-shirt.")
    print(f'It will say, "{message}"\n')

make_shirt('large', 'I love Python!')
make_shirt(message="Readability counts.", size='medium')

def describe_city(city, country='Chile'):
    """describe a city inside of a country"""
    print(f"{city.title()} is in {country.title()}\n")
describe_city('santiago')
describe_city('Reykjavik', 'Iceland')
describe_city('punta arenas')

def customer_info(first, last, city, dob):
    """describe the customer"""
    print(f"{first.title()} {last.title()} is from {city.title()} and was born on {dob}!\n")
customer_info('joe', 'pedersen', 'lake stevens', '11/02/93')