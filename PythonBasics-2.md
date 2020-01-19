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

# range()
print(range(100)) # range(0,100)

for number in range(0,10):
    print(number) # prints 0 - 9

for number in range(0,10,2):
    print(number) # prints 0,2,4,6,8

for number in range(0,10,-1):
    print(number) # prints nothing

for number in range(10,0,-2):
    print(number) # prints 10,8,6,4,2

for number in range(2):
    print(list(range(10))) # prints two arrays with values 0-9
    
# enumerate()
for i,char in enumerate('hello'):
    print(i, char) # prints every letter in string, as well as the index of each letter

for i,char in enumerate(list(range(100))):
  if(char == 50):
    print(f'The index of 50 is {i}')

# While Loops

i = 0
while i < 50:
    print(i) # prints infinetly

while i < 50:
    print(i)
    break # breaks the loop after 1 iteration

while i < 50:
    print(i)
    i += 1 # prints 0 - 49
    break
else:
    print('done with all the work')

# For vs While Loops

# For loops are simpler
my_list = [1,2,3]
for item in [1,2,3]:
    print(item)
    continue # brings you back top of the loop aka line 185
    print(item) # does not execute

# While loops have more flexibility
i = 0
while i < len([1,2,3]):
    print(my_list[i])
    i += 1

while True:
    print('something gets printed while the above condition is true')
    break

while True:
    response = input('say something: ')
    if (response == 'bye'):
        break

```

## Exercise: Tricky Counter
```Python
# Find the sum of values in a list

my_list = [1,2,3,4,5,6,7,8,9,10]
counter = 0

for item in my_list:
    counter += item
print(counter)
```

## Exercise: Creating a GUI

```Python
#Display the image below where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

for row in picture:
    for col in row:
      if col:
        print('*', end=' ')
      else:
        print(' ', end =' ')
    print()
```

## Exercise: Find Duplicates

```Python
# Check for duplicates in list:
duplicate_list = ['a','b','c','b','d','m','n','n']

duplicates = []

for letter in duplicate_list:
  if duplicate_list.count(letter) > 1:
    if letter not in duplicates:
      duplicates.append(letter)
print(duplicates)
```

## Functions

```Python
# defining a function with parameters
def say_hello(name, emoji):
    print(f'hello {name} {emoji}')

# calling the function with arguments
say_hello('Alex', ':)')
say_hello('Jim', ':)')
say_hello('Brandon', ':)')

# keyword arguments, bad practice as it is not very readable!
say_hello(emoji=':)', name='Bibi') # => hello Bibi :)

# defining a function with default parameters
def say_hello(name='Darth Vader', emoji= 'XD'):
    print(f'hello {name} {emoji}')

say_hello() # => hello Darth Vader XD

# return statement
def sum(num1, num2):
    def another_func(n1,n2):
        return n1 + n2
    return another_func(num1,num2)

total = sum(10,5)
print(total) # => 15
```

## Exercise: Check Drivers Age

```Python
age = input("What is your age?: ")

if int(age) < 18:
	print("Sorry, you are too young to drive this car. Powering off")
elif int(age) > 18:
	print("Powering On. Enjoy the ride!");
elif int(age) == 18:
	print("Congratulations on your first year of driving. Enjoy the ride!")

#1. Wrap the above code in a function called checkDriverAge(). Whenever you call this function, you will get prompted for age. 
# Notice the benefit in having checkDriverAge() instead of copying and pasting the function everytime?

def checkDriverAge():
    age = input("What is your age?: ")
    if int(age) < 18:
        print("Sorry, you are too young to drive this car. Powering off")
    elif int(age) > 18:
        print("Powering On. Enjoy the ride!");
    elif int(age) == 18:
        print("Congratulations on your first year of driving. Enjoy the ride!")

checkDriverAge()

#2 Instead of using the input(). Now, make the checkDriverAge() function accept an argument of age, so that if you enter:
#checkDriverAge(92);
#it returns "Powering On. Enjoy the ride!"
#also make it so that the default age is set to 0 if no argument is given.

def checkDriverAge(age=0):
    if int(age) < 18:
        print("Sorry, you are too young to drive this car. Powering off")
    elif int(age) > 18:
        print("Powering On. Enjoy the ride!");
    elif int(age) == 18:
        print("Congratulations on your first year of driving. Enjoy the ride!")

checkDriverAge() # => Sorry, you are too young to drive this car. Powering off
checkDriverAge(14) # => Sorry, you are too young to drive this car. Powering off
checkDriverAge(18) # => Congratulations on your first year of driving. Enjoy the ride!
checkDriverAge(70) # => Powering On. Enjoy the ride!
```

## Docstrings

```Python
def test(a):
    '''
    Info: this function tests and prints param a
    '''
    print(a)

test('!!!')
help(test()) # => test(a) Info: this function tests and prints param a (END)

print(test.__doc__) # => Info: this function tests and prints param a
```

## Clean Code

```Python
def is_even(num):
    if num % 2 == 0:
        return True
    return False

print(is_even(50)) # => True
print(is_even(51)) # => False
```

## *args & **kwargs

```Python
# *args
def super_func(args):
    return sum(args)

super_func(1,2,3,4,5) # => super_func() takes 1 positional argument but 5 were given

def super_func(*args, **kwargs):
    print(args) # => 1 2 3 4 5 
    print(*args) # => (1,2,3,4,5)
    return sum(args)

print(super_func(1,2,3,4,5)) # => 15

# **kwargs

def super_func(name, *args, i='hi', **kwargs):
    total = 0
    print(**kwargs) # => {'num1': 5, 'num2': 10}
    for items in kwargs.values():
        total += items
    return sum(args) + total

print(super_func('Andy', 1,2,3,4,5, num1=5, num2=10)) # => 30

# Rule: params, *args, default parameters, **kwargs
```

## Functions Exercise

```Python
def highest_even(li):
  highest = 0
  for num in li:
    if num % 2 == 0:
      if num > highest:
        highest = num
  return highest

print(highest_even([10,2,3,4,8,11])) # => 10
```