n = int(input("输入n:"))
a = n%3
b = n%5
if a == 0:
    if b == 0:
        print("类型: A")
    else:
        print("类型: B")
else:
    if b == 0:
        print("类型: C")
    else:
        print("类型: D")
        