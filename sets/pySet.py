#Defining a set
first_names = {'Adam','Beth','Charlie'}
print('Set of First Names: ' + str(first_names))

print('\n')

#Making a set from an existing list
my_list = [1,2,3]
print('Existing List: ' + str(my_list))
my_set = set(my_list)
print('Made Set: ' + str(my_set))

print('\n')

#Checking the membership of the set using 'in'
for name in first_names:
	print(name)

print('\n')

#Operations on sets
# a. With Other sets

## Intersection
print("## Intersection")
print({1,2,3,4,5}.intersection({3,4,5,6}))
print({1,2,3,4,5} & {3,4,5,6})
print("\n")

## Union
print("## Union")
print({1,2,3,4,5}.union({3,4,5,6}))
print({1,2,3,4,5} | {3,4,5,6})
print("\n")

## Difference
print("## Difference")
print({1,2,3,4,5}.difference({3,4,5,6}))
print({1,2,3,4,5} - {3,4,5,6})
print("\n")

## Symmetric Difference With
print("## Symmetric Difference With")
print({1,2,3,4}.symmetric_difference({2,3,5}))
print({1,2,3,4} ^ {2,3,5})
print("\n")

## Superset Check
print("## Superset Check")
print({1,2}.issuperset({1,2,3}))
print({1,2} >= {1,2,3})
print("\n")

## Subset Check
print("Subset Check")
print({1,2}.issubset({1,2,3}))
print({1,2} <= {1,2,3})
print("\n")

## Disjoint Check
print("Disjoint Check")
print({1,2}.isdisjoint({3,4}))
print({1,2}.isdisjoint({1,4}))
print("\n")

# b. With single elements

##Existance check
print("## Existance Check")
print(2 in {1,2,3})
print(4 in {1,2,3})
print(4 not in {1,2,3})

## Add and Remove
print("## Add and Remove")
s = {1,2,3}
s.add(4)
print(s)

print("\n")

s.discard(3)
s.discard(5)
print(s)

print("\n")

s.remove(2)
print(s)
# s.remove(2)
# print(s)

print("\n")