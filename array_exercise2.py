heroes=['spider man','thor','hulk','iron man','captain america']

#Length of the list
print(len(heroes))

#Add 'black panther' at the end of this list
heroes.append('black panther')
print(heroes)

#You realize that you need to add 'black panther' after 'hulk',
#so remove it from the list first and then add it after 'hulk'
heroes.remove('black panther')
heroes.insert(3,'black panther')
print(heroes)

#Now you don't like thor and hulk because they get angry easily :)
#So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#Do that with one line of code.
heroes[1:3]=['doctor strange']
print(heroes)

#Sort the heros list in alphabetical order
heroes.sort()
print(heroes)