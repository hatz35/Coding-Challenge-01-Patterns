rows = 14
current_space = 6
steps = 2
col = 2
hc = False
for i in range(rows):
    for i in range(2):
        for j in range(current_space):
            print(" ", end = "")
        for i in range(col):
            print(0, end = "")
        for j in range(current_space):
            print(" ", end = "")
        print()
    if current_space == 0:
        hc = True
    if hc:
        current_space += steps
        col -= 2*steps
    else:
        current_space -= steps
        col += 2*steps
