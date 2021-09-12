int_var = 100
print(type(int_var))
#integer variable type
str_var = '100'
print(type(str_var))
#string variable type

big_string = '''Hello, my name is Bob.
I like dogs and cats.'''
print(big_string)
#to use a multi line string you need triple quotes
big_string = 'Hello, my name is Bob.\nI like dogs and cats.'
print(big_string)
#or you can just use \n

print(big_string.replace("Bob", "Bobby"))
#cool string operation, I looked over many more, this one is my favorite

print(len(big_string))
#returns lenght of big_string