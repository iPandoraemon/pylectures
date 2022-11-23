'''
输入整数n(n<10), 求前n个同构数 (一整数若正好为其平方数的尾部, 则称该数为同构数,
 例如, 5正好是25的尾部, 故5为同构数), 程序运行效果如下。

提示: 若str(i*i).endswith(str(i))为真, 则i为同构数。

n=6
NO1:5
NO2:6
NO3:25
NO4:76
NO5:376
NO6:625
'''
s = input("n=")
if s.isdigit() & int(s)<10:
    n = int(s)
else:
    print("输入错误！")

cnt, i = 0, 1
isomor_nums = []
while cnt <= n:
    if str(i*i).endswith(str(i)):
        isomor_nums.append(i)
        cnt += 1        
    i += 1

for i in range(n):
    print("NO%d:%d" %(i, isomor_nums[i]))
