'''
已知a,b,c中存有1000以内能被3、5、7整除的整数, 试求1000以内Q1: 能被3且不能被
5整除的数的个数, Q2: 能被3和5整除但不能被7整除的数的个数, Q3: 能被3或5整除, 且
同时能被7整除的数的个数。
'''
a={i for i in range(0,1000,3)}
b={i for i in range(0,1000,5)}
c={i for i in range(0,1000,7)}
print("Q1:"+str(len(a-b)))
print("Q2:"+str(len(a&b-c)))
print("Q3:"+str(len(((a|b)&c))))
