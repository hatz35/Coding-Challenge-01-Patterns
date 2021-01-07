gapd = 0
gapdr = False
for i in range(5):
    print("*", end = "  ")
    print("*", end = "")
    for j in range(gapd):
        print(" ", end = "")
    print("*", end = "")
    for k in range(4-gapd):
        print(" ", end = "")
    print("*", end = "")
    for j in range(2-gapd):
        print(" ", end = "")
    print("*", end = "")
    print()
    if gapd == 2:
        gapdr = True
    if gapdr == False:
        gapd += 1
    else:gapd -=1
