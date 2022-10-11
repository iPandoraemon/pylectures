# 2（2）输入正整数n，求分数序列:2/1，3/2，5/3，8/5，13/8...的前n项的和值，结果保留4位小数。
n = eval(input('n='))
sum = 0.0
numerator = 2
denominator = 1
for i in range(n):
  sum += numerator/denominator
  numerator, denominator = numerator+denominator, numerator
print('s=%.4f'%sum)