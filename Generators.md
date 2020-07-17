# Generators

```Python
# range(100)  # => doesn't hold data in memory
# list(range(100))  # => holds data in memory


def make_list(num):
    result = []
    for i in range(num):
        result.append(i*2)
    return result  # => data is held in memory


my_list = make_list(100)  # => data is held in memory
print(my_list)
```
```Python
# Iterable  # => an object that can be looped over
# Generators  # => Iterable items

range()  # => generator
list()  # => iterable


def generator_function(num):
    for i in range(num):
        yield i*2


for item in generator_function(1000):
    print(item)  # => prints every item, holding only one number in memory at a time
    
g = generator_function(100)
print(g)  # => <generator object generator_function at 0x000002BFDC5FC3C0>
print(next(g))  # => 0
print(next(g))  # => 2
print(next(g))  # => 4
```