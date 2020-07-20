# my_file = open('test.txt')
#
# print(my_file)  # <_io.TextIOWrapper name='test.txt' mode='r' encoding='cp1252'>
#
# #  Reads entire file
# print(my_file.read())  # hi my name is alex costan
# my_file.seek(0)  # starts cursor back to the first line of the .txt file
# print(my_file.read())  # hi my name is alex costan
# my_file.seek(0)  # starts cursor back to the first line of the .txt file
# print(my_file.read())  # hi my name is alex costan
#
#
# #  Reads one line at a time
# print(my_file.readline(()))  # hi my name is alex costan
# print(my_file.readline(()))  # :)
# print(my_file.readline(()))  # how are you?
#
# #  Reads all the lines
# print(my_file.readlines())  # ['hi my name is alex costan\n', ':)\n', 'how are you?']
#
# #  Good practice when finished using file
# my_file.close()


# Proper way to work with Python files

# r mode allows read access to file
with open('test.txt', mode='r') as my_file:
    print(my_file.readlines())  # ['hi my name is alex costan\n', ':)\n', 'how are you?']

# w mode allows write access to file
with open('test.txt', mode='w') as my_file:
    text = my_file.write(':)')  # overwrites entire file in 'w' mode
    print(text)  # 2

# w mode also creates a new file if it doesn't exist already
with open('sad.txt', mode='w') as my_file:
    text = my_file.write(':(')
    print(text)  # 2

# r+ mode allows read and write permissions to the file
with open('test.txt', mode='r+') as my_file:
    print(my_file.readlines())  # ['hi my name is alex costan\n', ':)\n', 'how are you?']
    text = my_file.write(':)')  # appends ':)' to the end of file in 'r+' mode

# 'a' mode allows appending to files
with open('test.txt', mode='a') as my_file:
    text = my_file.write(':)')  # appends ':)' to end of file in 'a' mode
    print(text)  # 2
