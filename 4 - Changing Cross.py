import time
num = 1
rows = 9
print()
def clear_screen():
    print("\033[H\033[J")

while True:
    for i in range(1, rows+1):
        if i == 5:
            for o in range(9):
                print(num, end = " ")
        else:
            for j in range(4):
                print(" ", end = " ")
            print(num, end = " ")
            for k in range(4):
                print(" ", end = " ")
        print()
    if num == 9:
        num = 1
    else:
        num += 1
    time.sleep(1)
    clear_screen()
