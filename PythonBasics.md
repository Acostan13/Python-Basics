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

# bool
# str
# list
# tuple
# set
# dict

# Classes -> custom types

# Specialized Data Types
None
