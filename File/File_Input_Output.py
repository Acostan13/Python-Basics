my_file = open('test.txt')

print(my_file)  # <_io.TextIOWrapper name='test.txt' mode='r' encoding='cp1252'>

#  Reads entire file
print(my_file.read())  # hi my name is alex costan
my_file.seek(0)  # starts cursor back to the first line of the .txt file
print(my_file.read())  # hi my name is alex costan
my_file.seek(0)  # starts cursor back to the first line of the .txt file
print(my_file.read())  # hi my name is alex costan


#  Reads one line at a time
print(my_file.readline(()))  # hi my name is alex costan
print(my_file.readline(()))  # :)
print(my_file.readline(()))  # how are you?

#  Reads all the lines
print(my_file.readlines())  # ['hi my name is alex costan\n', ':)\n', 'how are you?']

#  Good practice when finished using file
my_file.close()
