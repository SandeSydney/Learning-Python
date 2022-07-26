state_capitals = {
    'Kenya' : 'Nairobi',
    'Tanzania' : 'Dodoma',
    'Burundi' : 'Bujumbura'
}
print('Dictionary of state capitals:')
print(state_capitals)
print('\n')

#finding the Kenyan capital
ke_capital = state_capitals['Kenya']
print('Capital of Kenya: ' + str(ke_capital) + '\n')

#getting all keys from a dictionary and iterating over them
print('#Getting keys from a dictionary and iterating over them')
for k in state_capitals.keys():
    print('{} is the capital of {}'.format(state_capitals[k], k))
print('\n')

#Getting all values from the dictionary
print(state_capitals.values())