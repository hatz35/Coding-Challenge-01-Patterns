num = 100
def printer(num):
        if num < 10:
            print(f"00{num}", end = " ")
        elif num ==100:
            print(num, end = " ")
        else:print(f"0{num}", end = " ")

for i in range(1, 11):
    for j in range(1, 11):
        printer(num)
        if j == 10:
            break
        elif i%2 ==0:
            num += 1
        else:
            num -= 1
    num -= 10
    print()
