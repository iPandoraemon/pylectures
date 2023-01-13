'''
现有一个判断n是否为素数的函数Prime(n), 若n为素数, 函数返回True, 否则返回False。

试利用该函数验证哥德巴赫猜想 (任何一个偶数均能表示为两个素数的和的形式)。输入整数a, 试将从a开始
的前5个偶数展开成两个素数的和的形式, 程序运行效果如下:

验证起点:101
102=5+97
104=3+101
106=3+103
108=5+103
110=3+107
'''

def Prime(n):   #判断n是否为素数
    re=True
    m=int(n**0.5)   # n=2: n**0.5=2**0.5=1.41423..., n=100: n**0.5=10.0-->10
    for i in range(2,m+1):      # n=2: 空的序列; n=10: 2, 3, 4, ..., 10 非空序列
        if n%i==0:
            re=False
            break
    return re


def Goldbach(m):                        #将偶数m展开成两个素数的和形式
    print(str(m)+"=",end="")
    i=2                                 #局部变量i （P181）
    while i<m:
        if Prime(i) and Prime(m-i):       #判断i与m-i是否同时为素数 m = i+(m-i) --> True and False
            print("%d+%d"%(i,m-i)) 
            break
        else:                           #找下一组的素数对
            i=i+1


def main():
    a=int(input("验证起点:"))    # '101'-->101
    if a%2>0:                   # 是否是偶数？
        a=a+1                   # 找到第一个偶数, a=102, a+10=112
    for i in range(a,a+10,2):   # i = 102, 104, 106, 108, 110
        Goldbach(i)


main()
