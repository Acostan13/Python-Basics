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

    @classmethod
    def adding_things(cls, num1, num2):
        return cls(num1 + num2)

    @staticmethod
    def adding_things2(num1, num2):
        return num1 + num2


print(PlayerCharacter.adding_things(2, 3))  # => <__main__.PlayerCharacter object at 0x0000028749D56A60>
player3 = PlayerCharacter.adding_things(2, 3)
print(player3.adding_things2(3, 4))

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


## Encapsulation

```Python
class PlayerCharacter:
    def __init__(self, name='anonymous', age=0):
        if age > 18:
            self.name = name
            self.age = age

    def run(self):
        print('run')
    
    def speak(self):
        print(f'my name is {self.name}, and I am {self.age} years old')
    
player1 = PlayerCharacter('Alex', 28)
player1.speak()  # => my name is Alex, and I am 28 years old
print(player1.name)  # =>  Alex
print(player1.age)  # =>  28

player2 = {'name': 'Jay', 'age': 24}
print(player2['name'])  # =>  Jay
print(player2['age'])  # =>  24
```

## Abstraction

```Python
class PlayerCharacter:
    def __init__(self, name, age):
        if age > 18:
            self._name = name  # private attributes
            self._age = age  # the underscore signifies privacy, a practice implented to notify coders NOT to reassign value

    def run(self):
        print('run')
    
    def speak(self):
        print(f'my name is {self._name}, and I am {self._age} years old')
```

## Inheritance

```Python
class User:
    def sign_in(self):
        print('logged in')

class Wizard(User):  # Inheriting User Class, subclass
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')

class Archer(User):  # subclass
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacking with arrows: arrows left - {self.num_arrows}')

wizard1 = Wizard('Merlin', 50)
archer1 = Archer('Robin', 100)

print(isinstance(wizard1, Wizard))  # => True
print(isinstance(wizard1, object))  # => True
print(isinstance(wizard1, User))  # => True because wizard1 is an instance of a subclass of User


print(wizard1)  # => Wizard object
wizard1.sign_in()  # => logged in

wizard1.attack()  # => attacking with power of 50
archer1.attack()  # => attacking with arrows: arrows left - 100
```