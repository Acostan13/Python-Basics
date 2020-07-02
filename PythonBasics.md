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
```

# Tuples

# Sets

# Dicts

# Classes -> custom types

# Specialized Data Types

None
