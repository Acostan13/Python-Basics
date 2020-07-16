# Decorators
```Python
def hello():
    print('hello')


greet = hello
print(greet())  # => hello , None
del hello
print(greet())  # => hello, None


def hi(func):
    return func()


def greet():
    print('still here!')


a = hi(greet)
print(a)  # => still here!, None
```
```Python
# Decorator Pattern
def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print('*****')
        func(*args, **kwargs)
        print('*****')
    return wrap_func


@my_decorator
def hello(greeting, emoji=':('):
    print(greeting, emoji)


@my_decorator
def bye(goodbye):
    print(goodbye)


hello('hi', ':)')
bye('see you later')
```
```Python
from time import time

def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'it took {t2-t1} seconds')
        return result
    return wrapper

@performance
def long_time():
    for i in range(100000000):
        i*5

long_time()
```

## HOC - Higher Order Functions
- A function that accepts within its parameters another function
- A function that returns another function
- map(), filter(), reduce() are all HOC's

```Python
def greet(func):
    func()


def greet2():
    def func():
        return 5
    return func
```