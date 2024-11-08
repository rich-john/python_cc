# CHECK FOR EQUALITY # 
# car = home
# car == home
# true

# equality tests are case sensitive, so;
# car = 'Audi' 
# car.lower() == 'audi'
# True

# CHECK FOR INEQUALITY # 
# != 

requested_topping = 'mushrooms'

if requested_topping != 'achovies':
  print("hold the anchovies")
  
# NUMERICAL COMPARISIONS # 
# AND

requested_toppings = ['ham']
'ham' in requested_toppings


banned_users = ['mary']
user = 'chris'

if user not in banned_users:
  print(f"{user.title()}, you can login.")
  
car = 'bmw'
print("is car == 'bmw'? I predict yes!")
print('this is an example')