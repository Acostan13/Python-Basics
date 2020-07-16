# Errors in Python
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