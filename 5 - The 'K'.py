
gap = 3
rows = 7
rev = False
for i in range(rows):
    print("*", end = "")
    for k in range(gap):
        print(" ", end = "")
    print("*", end = "")
    print()
    if gap == 0:
        rev =  True
    if rev:
        gap += 1
    else:
        gap -= 1

#different method
for i in range(7):
    for j in range(7):
        if j == 0 or i - j == 3 or i + j == 3:
            print("*", end="")
        else:
            print(end=" ")
    print()
