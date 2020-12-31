c1 = 0
c2 = "*"
rows = 11
space = 5
exspace = 0
ct = 1
rev = False
for i in range(rows):
    for i in range(space):
        print(c1, end = "")
    for j in range(ct):
        print(c2, end = "")
        for jj in range(exspace):
            print(c1, end = "")
        if exspace != 0:
            print(c2, end = "")
    for k in range(space):
        print(c1, end = "")

    if exspace == 9:
        rev = True
    if rev == False:
        space -= 1
        if exspace == 0:
            exspace += 1
        else:
            exspace += 2
    else:
        space += 1
        if exspace == 1:
            exspace -= 1
        else:
            exspace -= 2
    print()
