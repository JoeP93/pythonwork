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

#describing albums and when they are dropping
def make_album(Artist, Title, Dropdate):
    """Describe the Album"""
    print(f"{Artist.title()}'s new album {Title.title()} is coming out {Dropdate}!\n")
make_album('Morgan Wallen', 'Backside Country', '2/2/2028')
make_album('Drake', 'Take Care', '10/22/29')
make_album('Kendrick Lamar', 'DAMN', '7/10/30')

#Building a dictionary containing information about an album
def make_album(artist, title):
    """Build a dictionary that stores information about an album"""
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
    }
    return album_dict

album = make_album('Drake', 'Take Care')
print(album)
album = make_album('Kendrick lamar', 'DAMN')
print(album)
album = make_album('Morgan Wallen', 'Backside Country')
print(album)

#prepare the prompts
title_prompt = "\nWhat album are you thinking of? "
artist_prompt = "\nWho's the Artist? "

#Let the user know how to quit
print("Enter 'quit' at any time to stop.")

while True:
    title = input(title_prompt)
    if title == quit :
        break
    artist = input(title_prompt)
    if artist == 'quit' :
        break
    album = make_album(artist, title)
    print(album)

    print("\nThanks for repsonding")