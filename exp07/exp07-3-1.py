'''
数字对称金字塔显示, 输入n(n<10),显示数字对称金字塔的前n行, 程序运行效果如下：

n=6
     1
    121
   12321
  1234321
 123454321
12345654321
第i行：n-i个空格，左半部分i个数字，右半部分i-1个倒序的数字
'''
import string

s = input("n=")
if s.isdigit() & int(s)<10:
    n = int(s)
else:
    print("输入错误！")

numbers = string.digits[1:]  # numbers='123456789'
for i in range(1, n+1):      # i = 1, ..., n (n=6)
    # 首先打印前面的空格，然后打印金字塔前半部分，最后打后半部分
    # n-i个空格
    # numbers[:i]：前半部分的字符，第0个元素直到第i个元素之前
    print(" "*(n-i)+numbers[:i]+numbers[:i-1][::-1])