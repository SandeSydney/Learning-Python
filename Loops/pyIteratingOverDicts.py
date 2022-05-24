# Having the dict as below

d = {"a":1,"b":2,"c":3}

# to iterate through its keys:
for key in d:
    print(key)
print("\n")

# Above is equivalent to:
for key in d.keys():
    print(key)
print("\n")

# Iterating over the dict's values be like:
for value in d.values():
    print(value)
print("\n")

## Iterating over keys and values
for key, value in d.items():
    print(key, "::", value)