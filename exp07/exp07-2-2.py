'''
从键盘输入n (n<10), 输出九九乘法表的前n行的结果（每项乘积式占8列宽度，左对齐）

n=7

i j     j=1     j=2 ...                                 j=n
i=1     1*1=1   1*2=2   1*3=3   1*4=4   1*5=5   1*6=6   1*7=7   
i=2             2*2=4   2*3=6   2*4=8   2*5=10  2*6=12  2*7=14  
i=3                     3*3=9   3*4=12  3*5=15  3*6=18  3*7=21  
i=4                             4*4=16  4*5=20  4*6=24  4*7=28  
i=5                                     5*5=25  5*6=30  5*7=35  
i=6                                             6*6=36  6*7=42  
i=7                                                     7*7=49
第i行打印n-(i-1)个公式
第i行打印8*(i-1)个空格
'''
s=input("n=")   # input函数返回的是字符串
if (not s.isdigit()) & int(s)>=10:
    print("输入错误")
else:
    n=int(s)        # 转成整型
    for i in range(1,n+1):    # i=1, 2, ..., n
        print(" "*8*(i-1),end="")      #显示每行前面的空位
        for j in range(i,n+1):         #显示第i行上的所有乘积式 i=1, j=1, ..., n(n=7); i=2, j=2, ..., n(n=7)
            print("%-8s"%(str(i)+"*"+str(j)+"="+str(i*j)),end="")  #显示第j列一个乘积式
        print()     # 相当于是一个换行操作
