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

# ---------------------------------

regex = re.compile(r"([a-zA-Z]).([a])")
string = 'search this inside of this text please!'

a = regex.search(string)
print(a.group())  # => sea
print(a.group(1))  # => s
print(a.group(2))  # => a

testString = 'Hey are are you?'
regex2 = re.compile('^Hey')  # ^ asserts position at start of a line

b = regex2.search(testString)  # Hey (in testString) matches the characters Hey (in regex2) literally
print(b.group())  # => Hey
```

## Exercise: Passowrd Validation
### Create a Password that is at least 8 characters long, can contain any sort of numbers, letters, and @#$% 

```Python
import re

passwordVerifier = re.compile(r"([a-zA-Z0-9#@%$]{7,}[0-9])")

test_str1 = "DeAeG%"
test_str2 = "DeAeGae#"
test_str3 = "DeAeGae#$%@d53"

check1 = passwordVerifier.fullmatch(test_str1)  
check2 = passwordVerifier.fullmatch(test_str2)
check3 = passwordVerifier.fullmatch(test_str3)

print(check1)  # => None
print(check1)  # => None
print(check3)  # => <re.Match object; span=(0, 14), match='DeAeGae#$%@d53'>
```