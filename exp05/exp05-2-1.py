# 输入一个长度为奇数的整数元素列表，求列表中的元素最大值、最小值、平均值、中位数值
lb=eval(input("输入列表:"))
print("最大值="+str(max(lb)))
print("最小值="+str(min(lb)))
print("平均值=%g"%(sum(lb)/len(lb)))
lb.sort()
print("中位数=%d"%(lb[len(lb)//2]))
