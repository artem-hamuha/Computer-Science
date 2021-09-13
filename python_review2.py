def message():
    return 'Hi'

print(message())
#how to create/ print function

def message(x):
    return 'Hi ' + x

print(message("bob"))
#function that takes argumrnts(could take multiple arguments)S

def welcome(name='Artem', age="14"):
    return 'Welcome, you are {} and are {}'.format(name, age)

print(welcome('Bob'))
#you can also do things like this(set default parameters)