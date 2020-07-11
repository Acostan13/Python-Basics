# Object Oriented Programming

```Python
class PlayerCharacter:
    # Class Object Attribute
    membership = True

    def __init__(self, name='anonymous', age=0):
        if age > 18:
            self.name = name  # attributes
            self.age = age

    def shout(self):
        print(f'my name is {self.name}')


player1 = PlayerCharacter('Cindy', 44)
player2 = PlayerCharacter('Tom', 21)
player2.attack = 50

print(player1)  # <__main__.PlayerCharacter object at 0x000001FEFF6764C0>

print(player1.shout())  # my name is Cindy
print(player2.shout())  # my name is Tom

print(player1.name, player1.age)  # Cindy 44
print(player2.name, player2.age)  # Tom 21

print(player1.membership)  # True
print(player2.membership)  # True

print(player2.attack)  # 50
print(player1.attack)  # AttributeError: 'PlayerCharacter' object has no attribute 'attack'

help(player1)  # prints a blueprint of the object
```

## Exercise: Cats Everywhere

```Python
# Given the below class:
class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
purr = Cat(name='purr', age=3)
meow = Cat(name='meow', age=5)
rawr = Cat(name='rawr', age=1)

# 2 Create a function that finds the oldest cat


def oldest_cat(*kitty):
    return max(kitty)


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2

print(f'the oldest cat is {oldest_cat(purr.age, meow.age, rawr.age)} years old.')
```