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


```
