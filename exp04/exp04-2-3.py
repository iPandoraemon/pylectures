# 2（3）硬币兑换问题：将一笔零钱兑换成1分、2分、5分的硬币，要求每种硬币至少1枚，
# 从键盘上输入零钱的总数（整数，单位为分），显示这笔零钱可有的兑换方案数。
money  = eval(input('零钱数(分):'))
cnt = 0
for i in range(1, money//1+1):
  for j in range(1, money//2+1):
    for k in range(1, money//5+1):
      if i*1+j*2+k*5 == 20:
        cnt += 1
print('方案数:%d'%cnt)