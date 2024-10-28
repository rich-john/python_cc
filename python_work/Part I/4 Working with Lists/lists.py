magicians = ['alice', 'david', 'carolina']
for tits in magicians:
    print(magicians)

magicians = ['alice', 'david', 'caronlina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")

# range()
for value in range(1,5):
    print(value)
    
# list()
numbers = list(range(6))
print(numbers)

# skip numbers. the third agument tells python to skip by n
numbers = list(range(2,10,2))
print(numbers)

# making a list of squares. Note the indentation and the use of an empty list
squares = []
for value in range(1,10):
    square = value ** 2
    squares.append(square)
    
print(squares)

# Can be written more concisely. How? 

squares = []
for value in range(1,10):
    squares.append(value ** 2)
    
print(squares)

# min()
# max()
# sum ()

# list comprehensions
# Instead of multiline
squares = []
for value in range(1,10):
    square = value ** 2
    squares.append(square)
    
print(squares)

# do this
squares = [value**2 for value in range(1,11)]
print(squares)

## EXERCISES ##

for number in range(1,21):
    print(number)
    
for number in range(1,100000001):
    print(number)
    
numbers = list(range(1,1000001))
min(numbers)
max(numbers)
sum(numbers)
print(min(numbers)), print(max(numbers)), print(sum(numbers))

for odds in range(1,20,2):
    print(odds)

# Working with part of a list
# A specific group of items in a list is known as a slice

players = ['charles', 'martina', 'micheal', 'florence', 'eli']
print(players[0:3])

# If you omit the first index, python assumes you want the slice to start from the first index [0]
players = ['charles', 'martina', 'micheal', 'florence', 'eli']
print(players[:3])

# the same applies if you omit the 2nd index
players = ['charles', 'martina', 'micheal', 'florence', 'eli']
print(players[0:])

# say you wanted the last 3 elements added to a list 
players = ['charles', 'martina', 'micheal', 'florence', 'eli']
print(players[-3:])

# Looping through a slice 
players = ['charles', 'martina', 'micheal', 'florence', 'eli']
for player in players[:3]:
    print(player.title())
    
# omitting first and second arguement in a slice means put the entire list in a slice
players = ['charles', 'martina', 'micheal', 'florence', 'eli']
bad_players = players[:]



