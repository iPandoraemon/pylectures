# 2（1）输入一个年份区间，例如[1900,2015],求该区间内的闰年的个数。
# 闰年的判断：能被4整除但不能被100整除，或者能被400整除

a, b = eval(input('年份区间:'))
cnt = 0
for year in range(a, b+1):
  if year%4 == 0:
    if year%100 != 0:
      cnt+=1
    elif year%400 == 0:
      cnt+=1
print('闰年数='+str(cnt))