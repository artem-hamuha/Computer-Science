#I will use what I havee learned to create a little program
def welcome(name):
    if name == '':
        return 'Hame has not been entered'
    else:
        return 'Welcome {}'.format(name)

print(welcome('Bob'))