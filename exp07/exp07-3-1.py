'''
数字对称金字塔显示, 输入n(n<10),显示数字对称金字塔的前n行, 程序运行效果如下：

n=6
        1
       121
      12321
     1234321
    123454321
   12345654321
'''
import string

s = input("n=")
if s.isdigit():
    n = int(s)
else:
    print("输入错误！")

numbers = string.digits[1:]
for i in range(1, n+1):
    print(" "*(n-i)+numbers[:i]+numbers[:i-1][::-1])