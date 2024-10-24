bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# Accessing Elements in a List
print(bicycles[0])
print(bicycles[0].title())

# Index Positions Start at 0, Not 1
print(bicycles[1])
print(bicycles[3])

# Using Individual Values from a List
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)

# Changing, Adding, and Removing Elements
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

# Adding Elements to a List
motorcycles.append('honda')
print(motorcycles)

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

# Inserting Elements into a List
motorcycles.insert(0, 'ducati')
print(motorcycles)

# Removing Elements from a List
del motorcycles[0]
print(motorcycles)

# Removing an Item Using the pop() Method
popped_motorcycle = motorcycles.pop()
print(motorcycles)

print(popped_motorcycle)

last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")
print(motorcycles)

# Popping Items from any Position in a List
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")
print(motorcycles)

# Removing an Item by Value
motorcycles.remove('yamaha')
print(motorcycles)

# Removing an Item by Value
motorcycles.remove('ducati')
print(motorcycles)

# guest_list.py
guests = ['Albert Einstein', 'Isaac Newton', 'Galileo Galilei']
# print(f"Dear {guests[0]}, I would like to invite you to dinner.")
# print(f"Dear {guests[1]}, I would like to invite you to dinner.")
# print(f"Dear {guests[2]}, I would like to invite you to dinner.")

for guest in guests:
    print(f"Dear {guest}, I would like to invite you to dinner.")

print(f"\n{guests[0]} can't make it to dinner.")

# 1.3.3 Organizing a List
