## Using the return keyword in a loop in a function is like a break statement that breaks out of nested loops.
## Break alone cannot break nested loops but the loop level it is thererin

def break_loop():
    for i in range(1,5):
        if(i == 4):
            return (i)
        print(i)
    return 5

break_loop()

print("\n")

def break_all():
    for j in range(1, 5):
        for i in range(1, 4):
            if i * j == 6:
                return (i)
            print(i*j)

break_all()