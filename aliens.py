# if test passes the message will print - if NOT the message will not print
alien_color = 'green'
if alien_color == 'green':
    print("Congratulations you've earned 5 points!")
    # if the alien color is NOT green the message below will print!
else:
    print("Congratulations you've earned 10 points!")
# this is how to use if-elif-else statements to decifer the reward for a certain goal
alien1_color = 'red'
if 'purple' in alien1_color:
   print("Congrats you won 5 pts")
elif 'red' in alien1_color:
    print("congrats you won 10 pts")
else:
    print("congrats you won 15 pts")

# How to determine the stage of life you're in: (age is 21 so you are an adult)
age = 21
if age < 2:
    print("you're a baby")
elif age < 4:
    print("you're a toddler")
elif age < 13:
    print("you're a kid")
elif age < 20:
    print("you're a teenager")
elif age < 65:
    print("you're an adult")
else:
    print("you're an elder")