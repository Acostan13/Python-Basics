# Python Basics

## Fundamentals Data Types

```Python
int # => integer or a number

## type() gives the data's type
print(type(6)) # => <class 'int'>
print(type(2 - 4)) # => <class 'int'>
print(type(2 * 4)) # => <class 'int'>
print(2 ** 3) # => 8
print(5 // 4) # => 1
print(6 % 4) # => 2

float # => floating point number
print(type(2 / 4)) # => <class 'float'>, 0.5

complex # => Create a complex number from a real part and an optional imaginary part.
```

## Math Functions

```Python
## Round a number to a given precision in decimal digits.
print(round(3.1)) # => 3
print(round(3.9)) # => 4

## Return the absolute value of the argument.
print(abs(-20)) # => 20

## Return the binary representation of an integer and vice versa.
print(bin(5)) # => 0b101
print(int('0b101', 2)) # => 5
```

## Operator Precedence

### PEMDAS: Parenthesis, Exponents, Multiplication & Division, Addition & Subtraction

```Python
# PEMDAS
# ()
# **
# * /
# + -

print((20-3) + 2 ** 2) # => 21

print((5 + 4) * 10 / 2) # => 45.0

print(((5 + 4) * 10) / 2) # => 45.0

print((5 + 4) * (10 / 2)) # => 45.0

print(5 + (4 * 10) / 2) # => 25.0

print(5 + 4 * 10 // 2) # => 25
```

## Variables

- snake_case
- Start with lowercase or underscore
- Letters, numbers, underscores
- Case sensitive
- Don't overwrite keywords

```Python
#Declaring varialbes
user_iq = 190
print(user_iq) # => 190

_user_iq = 190 # => private variable
PI = 3.13 # => all upcase letters is a naming convention for constants

# Declaring multiple variables
a,b,c = 1,2,3
print(a) # => 1
print(b) # => 2
print(c) # => 3
```

## Strings

```Python
#Declaring Strings
username = 'supercoder'
passowrd = 'superrsecret'
long_string = '''
WOW
O O
---
'''

#String Concatenation
print('hello' + ' Alex') # => hello Alex
print('hello' + 5) # => TypeError: Can't add an int to a string
print(str(100)) # => 100

#Type Conversion
print(type(str(100))) # => <class 'str'>

#Escape Sequence
weather = "/t It\'s \"kind of\" sunny outside /n hope you have a good day!"
print(weather)  #    It's "kind of" sunny outside
                # hope you have a good day!

#Formatted Strings
name = 'Johnny'
age = 55

print(f'hi {name}. You are {age} years old') # => hi Johnny. You are 55 years old

#String Indexes
selfish = 'me me me'
         # 01234567

# [start:stop:stepover]
print(selfish[0]) # => m
print(selfish[7]) # => e
print(selfish[0:2]) # => me
print(selfish[0:8]) # => me me me
print(selfish[0:8:2]) # => m e m
print(selfish[1:]) # => me me me
print(selfish[:5]) # => me me
print(selfish[::1]) # => me me me
print(selfish[::-1]) # => em em em
print(selfish[::-2]) # => m m e
print(selfish[-1]) # => e
print(selfish[-4]) # => m

#Immutability - cannot change the value of a data type once it is created
# However, you can reassign variables to new values
selfish[0] = '8'
print(selfish) # => TypeError: 'str' object does not support item assignment
selfish += '8'
print(selfish) # => 12345678

#Built-In Functions + Methods
greet = 'hello'
print(len(greet)) # => 5
print(len(greet[0:len(greet)])) # => 5
print(len(greet[0:5])) # => 5

quote = 'to be or not to be'
print(quote.upper()) # => TO BE OR NOT TO BE
print(quote.capitalize()) # => To be or not to be
print(quote.find('be')) # => 3
print(quote.replace('be', 'me')) # => to me or not to me
```

# Booleans

```Python
name = 'Alex'
is_cool = False
is_cool = True

print(bool(1)) # => True
print(bool(0)) # => False
print(bool('True')) # => True
```

### Exercise: Type Conversion

```Python
name = 'John Smith '
age = 50
relationship_status = 'single'
relationship_status = "It's complicated"

# Take birth year input from your user, and print their age
birth_year = input('What year were you born?')
print(f"Your age is {2020 - int(birth_year)}")
```

### Exercise: Password Checker

```Python
username = input('Please enter your username:')
password = input('Please enter your password:')

pw_length = len(password)
hidden_pw = '*' * pw_length

print(f"{username}, your password, {hidden_pw}, is {pw_length} letters long")
```

# Lists

```Python
# Data Structure
li = [1,2,3,4,5]
li2 = ['a', 'b', 'c']
li2 = [1, 2, 'a', 'b', True]
print(li2[3]) # => b

# List Slicing
print(li2[0:2]) # => [1, 2]
print(li2[0::2]) # => [1, 'a', True]

# Lists are Mutable
li2[0] = 'hello'
print(li2) # => ['hello', 2, 'a', 'b', True]
print(li2[1:3]) # => [2, 'a']

# Modifying vs Copying Lists
li2[0] = 'hi'
new_list = li2 # modifying
new_list[0] = 'there'
print(li2) # => ['there', 2, 'a', 'b', True]
print(new_list) # => ['there', 2, 'a', 'b', True]

li2[0] = 'hi'
new_list = li2[:] # copying
new_list[0] = 'there'
print(li2) # => ['hi', 2, 'a', 'b', True]
print(new_list) # => ['there', 2, 'a', 'b', True]

# Matrix - 2D (or multi-dimensional) Lists
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print([0][1]) # => 2

# List Methods
# all of these methods modify lists, as opposed to copying them
basket = [1,2,3,4,5]
print(len(basket)) # => 5

# Appending
new_list = basket.append(100)
print(basket) # => [1,2,3,4,5,100]
print(new_list) # => None

# Inserting
bucket = [6,7,8,9,10]
bucket.insert(4,100)
new_bucket = bucket
print(bucket) # => [6,7,8,9,100,10]
print(new_bucket) # => [6,7,8,9,100,10]

# Extending
bucket = [6,7,8,9,10]
new_bucket = bucket.extend([100, 101])
print(bucket) # => [6,7,8,9,10, 100, 101]
print(new_bucket) # => None


# Removing
bucket = [6,7,8,9,10]
bucket.pop()
print(bucket) # => [6,7,8,9]
bucket.pop(0) # => [7,8,9]
basket.remove(8) # => [7,9]

bucket = [1,2,3,4,5]
new_bucket = bucket.pop(2)
print(new_bucket) # => 3

bucket = [1,2,3,4,5]
new_bucket = bucket.clear()
print(new_bucket) # => None
print(bucket) # => []

# Indexing
bucket = ['a','b','c','d',5]
print(bucket.index('c')) # => 2
print(bucket.index('d'), 0, 2) # => ValueError: 'd' is not in list
print('d' in bucket) # => True
print('x' in bucket) # => False
print('i' in 'hi my name is alex') # => True
print(bucket.count('d')) # => 1

# Sorting
bucket = ['a','x','b','c','d','e','d']
bucket.sort() # modifies list
print(bucket) # => ['a','b','c','d','d','e','x']

sortedBucket = sorted(bucket) # => creates a sorted copy of list
print(sortedBucket) # => ['a','b','c','d','d','e','x']

reversedBucket = sortedBucket.reverse() # => reverses the basket in place
print(reversedBucket) # => ['x','e','d','d','c','b','a']

# Copying Lists
bucket = ['a','x','b','c','d','e','d']
bucket.copy() # => creates a copy of bucket

# List Patterns
print(list(range(1,100))) # => Creates a list with numbers 1 - 99
print(list(range(101))) # => Creates a list with numbers 0 - 100

sentence = ' '.join(['hi','my','name','is','james'])
print(sentence) # => 'hi my name is james'

# List Unpacking
a,b,c, *other, d = [1,2,3,4,5,6,7,8,9]
print(a) # => 1
print(b) # => 2
print(c) # => 3
print(other) # => [4,5,6,7,8]
print(d) # => 9

# None
weapons = None
print(weapons) # => None

```

# Dictionaries - Unordered key value pairs

```Python
dictionary = {
    'a': [1,2,3],
    'b': 'hello',
    'c': True
}

print(dictionary['b']) # => hello
print(dictionary['a'][1]) # => 2

my_list = [
    {
        'a': [1,2,3],
        'b': 'hello',
        'x': True
    },
    {
        'a': [4,5,6],
        'b': 'hello',
        'x': True
    }
]

print(my_list[0]['a'][2]) # => 3

# Dictionary Methods

user = {
    'bucket': [1,2,3],
    'greet': 'hello'
}

# Get
print(user.get('age')) # => None
print(user.get('age'), 55) # => 55

user2 = dict(name='John')
print(user2) # => {'name': 'John'}

# keys() & values()
print('bucket' in user) # => True
print('size' in user) # => False
print('hello' in user.keys()) # => False
print('hello' in user.values()) # => True

# items()
print(user.items()) # => dict_items([('bucket, [1,2,3]),('greet', 'hello')])

# clear()
print(user.clear()) # => {}

# copy()
user2 = user.copy()
print(user) # => {'bucket', [1,2,4], 'greet': 'hello'}
print(user2) # => {'bucket', [1,2,4], 'greet': 'hello'}

# pop() & popitem()
print(user.pop('greet')) # => 'hello'
print(user) # => {'bucket', [1,2,4]}
print(popitem()) # => ('bucket', [1,2,4])
print(user) # => {}

# update()
print(user.update({'greet': 'hi'})) # => None
print(user) # => {'greet': 'hi'}
```

# Tuples

```Python
# Tuple - Like lists but they're immutable
my_tuple = (1,2,3,4,5)
my_tuple[1] = 'z' # => TypeError: 'tuple' object does not support item assignment
print(my_tuble[1]) # => 2
print(5 in my_tuble) # => True

# You can use Tuples within Dictionaries
user = {
    (1,2): [1,2,3],
    'greet': 'hello',
    'age': 20
}

print(user[(1,2)]) # => [1,2,3]

new_tuple = my_tuple[1:2]
print(new_tuple) # => (2,)

new_tuple2 = my_tuple[1:4]
print(new_tuple2) # => (2,3,4)

x,y,z, *other = (1,2,3,4,5)
print(x) # => 1
print(z) # => 2
print(y) # => 3
print(other) # => [4,5]

# Tuple Methods

# count() & index()
my_tuple = (1,2,3,4,5,5)
print(my_tuple.count(5)) # => 2
print(my_tuple.index(5)) # => 4

# len()
print(len(my_tuple)) # => 6

```

# Sets
```Python
# Sets - Unordered collections of unique objects

my_set = {1,2,3,4,5,5}
print(my_set) # => {1,2,3,4,5}
print(my_set[0]) # => TypeError: 'set' object does not support indexing
print(1 in my_set) # => True

# add(), copy() & clear()
my_set.add(100)
my_set.add(2)
print(my_set) # => {1,2,3,4,5,100}
print(len(my_set)) # => 6

new_set = my_set.copy()
my_set.clear()
print(new_set) # => {1,2,3,4,5}
print(my_set) # => set()

# set() & list()
my_list = [1,2,3,4,5,5]
print(set(my_list)) # => {1,2,3,4,5}
print(list(my_list)) # => [1,2,3,4,5]

# difference() & discard()
my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10}

print(my_set.difference(your_set)) # => {1,2,3}, difference() simply tells you the difference between two sets
print(my_set.discard(5)) # => None
print(my_set) # => {1,2,3,4}

# difference_update() - Removes all elements of another set from this set
my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10}

print(my_set.difference_update(your_set)) # => None, {4,5} are removed
print(my_set) # => {1,2,3}

# intersection() - Shows commonalities between two sets
my_set = {4,5}
your_set = {4,5,6,7,8,9,10}

print(my_set.intersection(your_set)) # => {4,5}
print(my_set & your_set) # => {4,5}, shorthand form

# isdisjoint() - Returns true if two sets have a null intersection
print(my_set.isdisjoint(your_set)) # => False

# union() - Returns a new set of concatenated sets without duplicates
print(my_set.union(your_set)) # => {1,2,3,4,5,6,7,8,9,10}
print(my_set | your_set) # => {1,2,3,4,5,6,7,8,9,10} shorthand form

# issubset() - Reports whether another set contains this set
print(my_set.issubset(your_set)) # => True

# issuperset() - Reports whether this set contains another set
print(your_set.issuperset(my_set)) # => True
```

# Classes -> custom types

# Specialized Data Types

None
