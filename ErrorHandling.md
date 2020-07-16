# Errors in Python
```Python
def hoooohoooo()
    pass

hoooohoooo()  # => SyntaxError


def hoooohoooo():
    1 + name


hoooohoooo()  # => NameError: name 'name' is not defined


def hoooohoooo():
    li = [1, 2, 3]
    li[5]


hoooohoooo()  # => IndexError: list index out of range


def hoooohoooo():
    di = {'a': 1}
    di['b']


hoooohoooo()  # => KeyError: 'b'


def hoooohoooo(num):
    5/num


hoooohoooo(0)  # => ZeroDivisionError: division by zero
```

## Error Handling

```Python
while True:
    try:
        age = int(input('what is your age? '))
        10/age
    except ValueError:
        print('please enter number')
        continue
    except ValueError:
        print('!!!!')
    except ZeroDivisionError:
        print('please enter an age higher than 0')
        break
    else:
        print('thank you!')
        break
    finally:
        print('ok, finally done')
    print('can you hear me?')  # => won't print


def sum1(num1, num2):
    try:
        return num1 + num2
    except TypeError as err:
        print(f'please enter numbers, {err}')


print(sum1('1', 2))  # => please enter numbers, can only concatenate str (not "int") to str
print(sum1(1, 2))  # => 3


def sum2(num1, num2):
    try:
        return num1 / num2
    except (TypeError, ZeroDivisionError) as err:
        print(err)


print(sum2(1, 0))  # => division by zero
print(sum2(1, '2'))  # => unsupported operand type(s) for /: 'int' and 'str'
```

## Raising Errors

```Python
while True:
    try:
        age = int(input('what is your age? '))
        10/age
        raise ValueError('hey cut it out')  # purposefully throws error into console
        raise Exception('stop it already!')
    except ZeroDivisionError:
        print('please enter an age higher than 0')
        break
    else:
        print('thank you!')
        break
    finally:
        print('ok, finally done')
```
