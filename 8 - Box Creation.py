import time

def clear_screen():
    print("\033[H\033[J")

print()
strength = 1
max_strength = 8
pp = [1]
while True:
    if max_strength != strength:
        for i in range(strength):
            if i == 0:
                for j in range(strength-1):
                    print("#", end = " ")
            print("#")
        strength += 1
    else:
        for i in range(8):
            if i == 0:
                for j in range(strength-1):
                    print("#", end = " ")
            elif i == 7:
                for j in range(pp[0]):
                    print("#", end = " ")
            elif i in pp:
                print("#", end = " ")
                for j in range(5):
                    print(" ", end = " ")
                print("#", end = " ")
            else:
                print("#", end = " ")
            print()
        if pp[0] != 7:
            pp[0] += 1
            pp.append(pp[0]-1)
        else:
            break

    clear_screen()
