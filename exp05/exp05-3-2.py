# 输入某同学本学期多门课程的成绩（每行输入1门课程成绩，以#作为输入的结束），
# 试以行方式显示其所有成绩，以及不及格课程的门数和相应的成绩.
# 要求：若没有不及格课程，则只显示成绩，不显示不及格课程等信息。

print("输入成绩（以#结束）：")

# 输入多门课程成绩，每行1门成绩，以#结束
scores = []
while True:
    scr = input()
    if scr == '#':
        break
    else:
        scores.append(float(scr))
print("成绩", scores)


# 统计不及格课程及记录不及格分数
gradeF = []
for item in scores:
    if item < 60:
        gradeF.append(item)

if len(gradeF) > 0:
    print("不及格课程门数:", len(gradeF))
    print("不及格成绩分别为:", end="")
    
    # 打印不及格分数，常规写法：
    for i in range(len(gradeF)):
        if i == len(gradeF)-1:
            print(gradeF[i], end="")
        else:
            print(gradeF[i], end=",")
    # 另一种写法如下，更加简洁，供参考！
    # print(*gradeF, sep=',')
    
