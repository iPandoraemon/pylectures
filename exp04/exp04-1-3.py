# 1（3）输入m,n两个整数，利用欧几里得定律求这两个整数的最大公约数
m,n=eval(input("输入m,n:"))
r=m%n
while r>0:
  m=n
  n=r
  r=m%n
print("最大公约数:"+str(n))
