# How to test whether or not statements are true or false
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False")
print(car == 'audi')

cue = 'meucci'
print("Is cue == meucci")
print(cue == 'meucci')
(print("\nIs cue predator?"))
print(cue == 'predator')

name = 'Joe'
print("\nis my name Jimmy?")
print(name == 'Jimmy')
print("\nIs my name Joe?")
print(name == 'Joe')

# Testing for Equality
print("\nDoes the first pizza match the second pizza in size?")
pizza = 'Large'
pizza1 = 'Large'
pizza2 = 'Small'
print(pizza == pizza1)
print("the first and second pizzas are different in size, huh?")
print(pizza != pizza1) #same size so comes up false
print("\nDoes the first pizza match the third pizza in size?")
print(pizza == pizza2)
print("the first and last pizzas are different in size, huh?")
print(pizza != pizza2) #different size pizzas so comes up true!

#testing the lower method
cue = 'Meucci'
cue.lower() == 'muecci'
print(cue.upper())