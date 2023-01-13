'''
利用前面一(1)题中的素数判别函数Prime(n), 编写程序找出[a,b]区间内的所有孪生素数
（若两个素数之差为 2, 则这两个素数就是一对孪生素数, 例如: 3和5、5和7、11和13等
都是孪生素数), 程序运行效果如下:

输入a,b:100,200
孪生素数对如下:
101 103
107 109
137 139
149 151
179 181
191 193
197 199
'''

def Prime(n):   #判断n是否为素数
    re=True
    m=int(n**0.5)   
    for i in range(2,m+1):
        if n%i==0:
            re=False
            break
    return re


def TwinPrime(x):
    re = True
    if Prime(x) and Prime(x+2):
        print("%d %d" %(x, x+2))


a, b = eval(input("输入a,b:"))
print("孪生素数对如下:")
for i in range(a, b-1): # i = a, a+1, a+2, ..., b-3, b-2; 假如b-2是素数，我们判断b是否是素数
    TwinPrime(i)