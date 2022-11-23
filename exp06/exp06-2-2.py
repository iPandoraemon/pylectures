'''
随机数生成与统计问题, 要求生成100个[0,9]范围内的随机整数, 
并统计不同数字出现的次数, 按生成的随机数升序输出。
'''

from random import randint
nums = [randint(0,9) for i in range(100)] 
numset = set(nums)                #得到随机数集合（确保每个数出现的唯一性）
result = {}                        #保存统计结果的空字典
for i in numset:                  #统计每个数出现的次数
    result[i] =  nums.count(i)
resultlist = sorted(result.items())  #按键(整数)升序排序
print("统计结果如下:")
for s in resultlist:
    print("%d:%d"%(s[0],s[1]))
