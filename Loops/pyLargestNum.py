## Using for loops to find the largest number 

lgst_so_far = None
print('Before', lgst_so_far)
for num in [9,41,12,3,74,15]:
    if lgst_so_far is None:
        lgst_so_far = num
    elif num > lgst_so_far:
        lgst_so_far = num
    print(lgst_so_far, num)

print('After', lgst_so_far)
