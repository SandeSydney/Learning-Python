#To get unique elements of a list, first turn the list into a set

home_counties = ["Nairobi","Nakuru","Nairobi","Mombasa","Nakuru","Kajiado"]
unique_counties = set(home_counties)
print(unique_counties)

print("\n")

# The result set can be turned back into a list, same as previous but without duplicates
print(list(unique_counties))
print("\n")

# or can be done as... 

print(list(set(home_counties)))
print("\n")