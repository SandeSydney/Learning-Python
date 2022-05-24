## Finding the smallest number in a List

smallest_so_far = None
print('Before', smallest_so_far)
for value in [9,41,12,3,74,15]:
    ## We don't know the smallest number. The first loop captures the first value as the smallest
    if smallest_so_far is None:
        smallest_so_far = value
    elif value < smallest_so_far:
        smallest_so_far = value
    print(smallest_so_far, value)

print('After', smallest_so_far)