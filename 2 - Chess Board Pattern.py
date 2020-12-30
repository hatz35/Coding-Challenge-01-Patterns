wzbo = 1 #whitezeroblackone
rows = 8

def alter(n):
    if n == 1:
        return 0
    elif n == 0:
        return 1

for i in range(rows):
    for j in range(rows):
        print(wzbo, end = " ")
        wzbo = alter(wzbo)
    print()
    wzbo = alter(wzbo)
