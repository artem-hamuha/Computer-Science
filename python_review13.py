passwords = {'Dude' : 'dude123', 'User1508' : 'Hamburger_21'}
print(passwords['Dude'])
#I can asign keys to values using dictionarys

passwords['User1508'] = '@MIT_$ix'
print(passwords['User1508'])
#dictionarys are mutable

passwords['Bob'] = 'pass_login'
print(passwords)
del(passwords['User1508'])
print(passwords)
#deleating

my_dictionary = {'numbers' : [1,56,4,8,10,3,100], 
'my words' : ['like', 'I', 'he', 'she', 'they', 'them', 'me', 'python', 'we']}
print(my_dictionary['my words'][0])
#basiclly nested lists but lists inside dictionarys

people = {1 : 'John Green', 2 : 'Bob Gerald', 3 : 'Aiden Smith'}
print(people[1])
#you can use anything immutable as a key

dict = {x: x**2 for x in (2, 4, 6)}
print(dict)
#writing for loop in dictionary is useful

names = ('Josh', 'Gavin', 'Alice')
newborns = dict.fromkeys(names, 0)
print(newborns)
#dictfromkeys creates a dictionary based on the list of keys given

users = {'john':'253-899-7734', 'maggy': '286-541-6791', 'bob': '800-210-0000'}
tmobile_users = users.keys()
print(tmobile_users)
#view keys can also do values

x = {'x' : 1, 'y' : 2, 'm' : 3}
print(x.get('b', 10))
print(x.get('f'))
#using get returns none if not found instead of an error

users = {'john':'253-899-7734', 
        'maggy': '286-541-6791', 
        'bob': '800-210-0000'}
print(list(users))
#easy way to get all keys in order
print(sorted(users))
#returns keys in alphabetical order

print('john' in users)
print('john' not in users)
#cheking if john is in users

print(users.items())
for name, number in users.items():
    print(name,'-', number)
#for looping through dictionary

dict1 = {'a': 0}
dict2 = {'b': 1}
merged = dict1 | dict2
print(merged)
#merging 2 dictionaries

first_dict  = { 'a': 1, 'b': 2, 'c': 'a string' }
second_dict = { 'a': 1, 'b': 2, 'c': 'a string' }
print(first_dict == second_dict)
#comparing