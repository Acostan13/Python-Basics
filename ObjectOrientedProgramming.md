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
