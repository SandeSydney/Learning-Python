#Creating a List of names
name_list = ['Alice', 'Bob', 'Oliver', 'Crystal']
print('# The created list')
print(name_list)

#Adding a name to the list
name_list.append('Victor')
print('\n# Appending name on list')
print(name_list)

#Inserting a name to a specific position
name_list.insert(2, 'Fiona')
print('\n# Inserting name to specific position in list')
print(name_list)

#Remove specific item from the list
name_list.remove('Bob')
print('\n# Removing specific name from list')
print(name_list)

#Find the length of the list
print('\n# The size of the current list')
print(len(name_list))
print('\n')

#Counting occurrence of any item on list
int_list = [1,1,1,2,3,3,4]
print('Created List : ' + str(int_list))
print('\nNumber of occurrences of:')
print(' 1 : ' + str(int_list.count(1)) + ' times')
print(' 3 : ' + str(int_list.count(3)) + ' times')
print('\n')

#Reversing the list
print('List before Reversal: ' + str(int_list))
print('List after Reversal: '+ str(int_list[::-1]))
print('\n')

#Return and Remove item from index
print(name_list)
print('Remove and Return last name')
print(name_list.pop())
print('\n')

#Iterating over the elements in list
print('Iterating over elements in list ' + str(int_list))
for element in int_list:
	print (element)
print('\n')