# Object Oriented Programming

```Python
class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name  # attributes
        self.age = age

    def run(self):
        return 'run'


player1 = PlayerCharacter('Cindy', 44)
player2 = PlayerCharacter('Tom', 21)
player2.attack = 50

print(player1.run())  # run
print(player1)  # <__main__.PlayerCharacter object at 0x000001FEFF6764C0>
print(player1.name, player1.age)  # Cindy 44
print(player2.name, player2.age)  # Tom 21

print(player2.attack)  # 50
print(player1.attack)  # AttributeError: 'PlayerCharacter' object has no attribute 'attack'
```
