# this is how to quote someone or strip extra whitespace from a string
name= "Joe"
message = f"hello {name.lower()}, how are you today?"
print(message)
quote= "the bigger they are the harder they fall"
author= "One Eye Bill"
full_quote = f'{author} once said: "{quote}"'
print(full_quote)
famous_person = 'White Goodman'
message = f'A famous quote by {famous_person} is: "thats me taking the bull by the horns, its a mediphore"'
print(message)
name = "\tSam\n"
print(name)
print(f"{name.lstrip()}")
print(f"{name.rstrip()}")
print(f"{name.strip()}")
filename = "python_notes.txt"
filename_without_extension = filename.removesuffix('.txt')
print(filename_without_extension)