# 输入正整数n，利用列表求斐波拉契数列前n项，每行显示6项，每项占10列宽度
n = int(input())

shulie = [1, 1]
for i in range(2, n):
    shulie.append(shulie[i-2]+shulie[i-1])

print("%10d"%shulie[0], end="")
for i in range(1, n):
    if i%6 == 0:
        print("")
    print("%10d"%shulie[i], end="")
    
