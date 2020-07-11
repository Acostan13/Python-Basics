# Regular Expressions

```Python
import re

string = 'search inside of this text please!'

print('search' in string)  # => True

a = re.search('this', string)

print(a.span())  # => (17, 21)
print(a.start())  # => 17
print(a.end())  # => 21
print(a.group())  # => this

# ---------------------------------

string = 'search this inside of this text please!'
pattern = re.compile('this')
pattern2 = re.compile('search this inside of this text please!')
pattern3 = re.compile('search this inside of this text please! Alex')


a = pattern.search(string)  # => checks for a match
b = pattern.findall(string)  # => checks for all matches
c = pattern2.fullmatch(string)  # => checks for exact matches
d = pattern2.match(string)  # => checks for matches at the beginning of pattern

print(a.group())  # => this
print(b)  # => ['this', 'this']
print(c)  # => <re.Match object; span=(0, 39), match='search this inside of this text please!'>
print(d)  # => <re.Match object; span=(0, 39), match='search this inside of this text please!'>

```