'''
已知函数san(a,n)的功能是求从整数a开始的前n项的和值, 即san(2,4)=2+3+4+5。
现需要利用该函数求s=1+(2+3)+(3+4+5)+(4+5+6+7)...前m项的和值,程序运行效
果如下:

s = san(1,1)+san(2,2)+san(3,3)+san(4,4)
san(i, i)


m=4         # 调用多少次san函数
和值=40      # 结果打印出来
'''
def san(a,n):
    s=0             # 初始化和值变量s为0
    for i in range(a,a+n):  # i = a, a+1, a+2, ..., a+(n-1); i=1时, i只有一个元素为1; i=2时, i可取2, 3
        s=s+i
    return s


def fun(m):
    s=0             # 初始化和值变量s为0
    for i in range(1,m+1):  # i = 1, 2, ..., m
        s=s+san(i, i)   #将从i开始前i项的和累加到总和里面
    return s        # 返回求和值（整数型）


def main():
    n=int(input("m="))      # n = 4
    print("和值="+str(fun(n)))  # fun(4) --> san(1,1)...san(4,4), 求和值 --> 转译为字符串类型


main()