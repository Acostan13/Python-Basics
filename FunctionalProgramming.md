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


def only_odd(item):
    return item % 2 != 0


print(list(filter(only_odd, my_list)))  # => [1, 3]
```

## zip()

```Python
my_list = [1, 2, 3]
your_list = [10, 20, 30]
their_list = (5, 4, 3)

print(list(zip(my_list, your_list)))  # => [(1, 10), (2, 20), (3, 30)]
print(list(zip(my_list, your_list, their_list)))  # => [(1, 10, 5), (2, 20, 4), (3, 30, 3)]
```

## reduce ()

```Python
from functools import reduce

my_list = [1, 2, 3]


def accumulator(acc, item):
    print(acc, item)  # => 10 1, 11 2, 13 3
    return acc + item


print(reduce(accumulator, my_list, 10))  # => 16
```

## Exercises: map, filter, zip, reduce

```Python
from functools import reduce

# 1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']


def capitalization(pets):
    return pets.capitalize()


print(list(map(capitalization, my_pets)))  # => ['Sisi', 'Bibi', 'Titi', 'Carla']

# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]

print(list(zip(my_strings, sorted(my_numbers))))  # => [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)]

# 3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]


def highscores(score):
    return score > 50


print(list(filter(highscores, scores)))  # => [73, 65, 76, 100, 88]

# 4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?


def accumulator(acc, item):
    return acc + item


print(reduce(accumulator, (my_numbers + scores)))  # => 456
```

## Lambda Expressions

- Anonymous function

```Python
from functools import reduce

my_list = [1, 2, 3]

# lambda param: action(param)
print(list(map(lambda item: item*2, my_list)))  # => [2, 4, 6]
print(list(filter(lambda item: item % 2 != 0, my_list)))  # => [1, 3]
print(reduce(lambda acc, item: acc + item, my_list))  # => 6
```

## Exercise: Lambda Expressions

```Python
# Square every item in my_list

my_list = [5, 4, 3]
print(list(map(lambda item: item**2, my_list)))  # => [25, 16, 9]

# Sort by the second element of the tuple in the_list from lowest to highest

the_list = [(4, 3), (0, 2), (9, 9), (10, -1)]

the_list.sort(key=lambda x: x[1])
print(the_list)  # => [(10, -1), (0, 2), (4, 3), (9, 9)]
```

## List Comprehension

```Python
my_list = [char for char in 'hello']
my_list2 = [num for num in range(0, 100)]
my_list3 = [num*2 for num in range(0, 100)]
my_list4 = [num**2 for num in range(0, 100) if num % 2 == 0]

print(my_list)  # => ['h', 'e', 'l', 'l', 'o']
print(my_list2)  # => [0, 1, 2, ..., 99]
print(my_list3)  # => [0, 2, 4, ..., 198]
print(my_list4)  # => [0, 4, 16, ..., 9604]
```

## Set and Dictionary Comprehensions

```Python
my_list = {char for char in 'hello'}
my_list2 = {num for num in range(0, 100)}
my_list3 = {num*2 for num in range(0, 100)}
my_list4 = {num**2 for num in range(0, 100) if num % 2 == 0}

print(my_list)  # => {'e', 'o', 'h', 'l'}
print(my_list2)  # => {0, 1, 2, ..., 99}
print(my_list3)  # => {0, 2, 4, ..., 198}
print(my_list4)  # => {0, 256, 1024, ..., 7396}

simple_dict = {
    'a': 1,
    'b': 2
}
my_dict = {key: value**2 for key, value in simple_dict.items()}
print(my_dict)  # => {'a': 1, 'b': 4}

my_dict2 = {num: num*2 for num in [1, 2, 3]}
print(my_dict2)  # => {1: 2, 2: 4, 3: 6}
```
