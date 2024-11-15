'hello' == 'hello' # True
'hello' == 'Hello' # False
'hello' != 'hello' # False
'hello' != 'Hello' # True

string = 'hello'
print(string.lower() == 'hello') # True
print(string.lower() != 'hello') # False

1 == 1 # True
1 == 2 # False
1 != 1 # False
1 != 2 # True

1 > 0 # True
1 < 0 # False
1 >= 0 # True
1 <= 0 # False

1 > 0 and 1 < 0 # False
10 > 0 and 10 < 20 # True

number = [1, 2, 3, 4, 5]
print(1 in number) # True
print(6 in number) # False
print(6 not in number) # True
print(1 not in number) # False
