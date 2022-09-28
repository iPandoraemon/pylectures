print("***自由式滑雪评分***")
num=input("选手编号:")
a,b,c=eval(input("基础三项得分:"))      #以逗号为分隔符输入三个数据，以合适的类型分别赋给a,b,c
difficulty=float(input("难度系数:"))   #显示提示，输入一个字符串，并将将其转换成浮点数
score=(a*0.3+b*0.5+c*0.2)*difficulty  #计算得分
print("---------END---------\n")
print("---选手成绩---")
print("编号:"+num)
print("得分:"+str(score))
print("------------------")
