xcol = [6, 9]
halfdone = False
for row in range(1,15):
    for col in range(1,15):
        if col > xcol[0] and col < xcol[1]:
            print("row:", str(row), "col", str(col))

    if row == 8:
        halfdone = True

    if halfdone == False and row%2==0:
        xcol[0] -= 2
        xcol[1] += 2
    elif halfdone == True and row%2 == 0:
        xcol[0] += 2
        xcol[1] -= 2
