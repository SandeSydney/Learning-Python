#Keys for which value has not been explicitly defined can be accessed without errors

#Must import defaultdict from collections
from collections import defaultdict

#'Makindu' is what I want to be returned by default if key used isn't defined
state_capitals = defaultdict(lambda: 'Makindu')

#Now populating dictionary with key-value pairs
state_capitals['Kenya'] = 'Nairobi'
state_capitals['Uganda'] = 'Kampala'
state_capitals['Tanzania'] = 'Dodoma'
state_capitals['Nigeria'] = 'Lagos'

#Accessing the dictionary with a non-existent key
print('Using non-existent key: Congo')
print(state_capitals['Congo'])

print('\n')

print('Using existent key: Kenya')
print(state_capitals['Kenya'])