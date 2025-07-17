r = int(input('How many rows?: '))
total = 100
c = total // r
num=1
for i in range(r):
    for j in range(c):
        if num > 100:
            break
        print(f"{num:3}", end="")
        num += 1
    print()