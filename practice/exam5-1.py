def printstar(n):
    for x in range(0, n):
        for y in range(-n, n):
            if abs(x)+abs(y) <= n:
                print("*", end='')
            else:
                print(" ", end='')
            print()


printstar(10)