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