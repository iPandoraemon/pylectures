'''
编写函数jc(n), 函数的功能是求正整数n的阶乘, 并调用该函数求1!+2!+3!+…+m!的和值,
m为用户在界面上输入的值, 程序运行效果如下:

m=4
和值=33
'''

def jc(n):
    if n==0 or n==1:
        return 1
    else:
        r = n * jc(n-1)
        return r

m = int(input("m="))
print("和值=", end="")

#####################################################
# 以下两个方案取其中一个，注释其他方案的代码：
# ------------------------------
# 方案1(推导式法)：
# ------------------------------
# polynomial = [jc(i) for i in range(1, m+1)]  # [jc(1), ..., jc(m)]
# print(sum(polynomial))

# ------------------------------
# 方案2(循环求和法)：
# ------------------------------
s = 0
for i in range(1, m+1):
    s = s+jc(i)
print(s)

# 以上两个方案取其中一个，注释其他方案的代码：
#####################################################