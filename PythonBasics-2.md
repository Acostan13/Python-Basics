# Python Basics 2

## Conditional Logic

```Python
# Truthy and Falsy
is_old = True
is_licenced = True

if is_old and is_licenced:
    print('your are eligible to drive!')
elif is_old:
    print('you do not have a licence!')
elif is_licenced:
    print('you are not old enough to drive!')
else:
    print('you are not eligible to drive!')


username: 'johnny'
password: '123'

if password and username:
    print(f'Welcome, {username}!')
elif username:
    print('Incorrect Password')
else password:
    print('That username does not exist')

# Ternary Operator

is_friend = True
can_message = "message allowed" if is_friend else "not allowed to message"
print(can_message) # => message allowed

# Short Circuiting

is_Friend = True
is_User = False
if is_Friend or is_User: # prints message since is_Friend is True
    print('best friends forever')

# is vs == 

# == checks for equality in value
print(True == 1) # True
print('' == 1) # False
print('1' == 1) # False
print([] == 1) # False
print(10 == 10.0) # True
print([] == []) # True

# is checks the location in memory if the value is the same
print(True is 1) # False
print('' is 1) # False
print('1' is '1') # True
print([] is 1) # False
print(10 is 10) # True
print([1,2,3] is [1,2,3]) # False


# Logical Operators

print(4 < 5) # True
print(4 > 5) # False
print(4 == 5) # False
print('hello' == 'hello') # True
print('a' > 'A') # True, because it has a higher hexidecimal value on the ASCII Table
print(1 < 2 < 3 < 4>) # True
print(1 >= 0) # True
print(1 <= 0) # False
print(0 != 0) # False
print(not(True)) # True
print(not(1 == 1)) # False
```

## Exercise: Logical Operators

```Python
is_magician = False
is_expert = True

# Check if magician AND expert: "you are a master magician"
if is_magician and is_expert:
    print("You are master magician")

# Check if magician but not expert: "at least you're getting there"
elif is_magician and not is_expert:
    print("Atleast you're getting there")

# If you're not a magician: "You need magic powers"
elif not is_magician:
    print("You need magic powers")
```

## Loops

```Python
# For Loop
for letter in 'Zero to Mastery':
    print(letter) # prints every item in iterable
print(letter) # prints last item in iterable

# Nested For Loop
for number in (1,2,3,4,5):
    for x in ['a', 'b', 'c']:
        print(number, x) # prints inner loop iterable values once for every value in the outer loop iterable

# Iterable - Object or collection that can be iterated over
# Ex: list, dictionary, tuple, set, string
# Iterated => one by on check each item in the collection

# Looping over an Object
user = {
    'name': 'Golem',
    'age': 5006,
    'can_swim' = False
}

for item in user:
    print(item) # prints keys of object

for item in user.keys():
    print(item) # explicitly prints keys

for item in user.values():
    print(item) # prints values of object
    
for item in user.items():
    print(item) # prints keys/value pairs

for key, value in user.items():
    print(key, value) # explicitly prints keys/values

for item in 50:
    print(item) # TypeError: 'int' object is not iterable
```