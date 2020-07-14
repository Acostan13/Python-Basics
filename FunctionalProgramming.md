# Functional Programming
- Clear + Understandable
- Easy to Extend
- Easy to Maintain
- Memory Efficient
- DRY

## Pure Functions
- Given the same input, will always return the same output
- Produces no side effects.

```Python
def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    return new_list


print(multiply_by2([1, 2, 3]))  # => [2, 4, 6]
```

## map()

```Python
def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    return new_list


print(multiply_by2([1, 2, 3]))  # => [2, 4, 6]
print(map(multiply_by2, [1, 2, 3]))  # => <map object at 0x0000025AED2C3160>
```
```Python
my_list = [1, 2, 3]


def multiply_by2(item):
    return item*2


print(list(map(multiply_by2, [1, 2, 3])))  # => [2, 4, 6]
print(list(map(multiply_by2, [my_list])))  # => [2, 4, 6]
print(my_list)  # => [1, 2, 3]
```

## filter()

```Python
my_list = [1, 2, 3]


def multiply_by2(item):
    return item*2


def only_odd(item):
    return item % 2 != 0


print(list(filter(only_odd, my_list)))  # => [1, 3]
```

## zip()

```Python
my_list = [1, 2, 3]
your_list = [10, 20, 30]


def multiply_by2(item):
    return item*2


def only_odd(item):
    return item % 2 != 0


print(list(zip(my_list, your_list)))  # => [1, 3]
```