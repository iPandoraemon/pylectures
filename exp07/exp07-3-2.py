'''
输入整数n(n<10), 求前n个同构数 (一整数若正好为其平方数的尾部, 则称该数为同构数,
 例如, 5正好是25的尾部, 故5为同构数), 程序运行效果如下。

提示: 若str(i*i).endswith(str(i))为真, 则i为同构数。

5 --> 25  --> 5
25 --> 625 --> 25

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

isomor_nums = []    # 用一个列表保存同构数

# --------------------------
# 写法一：
cnt, i = 0, 2       # 初始化两个变量：计数器count、寻找同构数变量
# 寻找同构数
while cnt <= n:
    if str(i*i).endswith(str(i)):
        isomor_nums.append(i)   # 追加同构数
        cnt += 1                # 计数器+1      
    i += 1                      # 更新i

# --------------------------
# 写法二：
## 寻找同构数
# i = 2       # 初始化两个变量：计数器count、寻找同构数变量
# while len(isomor_nums) <= n:
#     if str(i*i).endswith(str(i)):
#         isomor_nums.append(i)
#     i += 1


for i in range(1, n+1):         # i = 1, ..., n
    print("NO%d:%d" %(i, isomor_nums[i-1]))
