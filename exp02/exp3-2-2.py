s=0
for i in range(7):            #循环7次，输入一周的营业收入
      a=float(input())       #每次输入一天的营业收入
      b=a-int(a)            #int()函数用于求浮点数的整数部分
      s+=b
print("money=%.2f"%s)     #输出和值s，保留2位小数
