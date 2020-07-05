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
