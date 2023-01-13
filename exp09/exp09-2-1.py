"""
已知学生姓名与成绩保存于stud.txt文件中(格式如下图), 
现已知录取分数线为305分, 请按照文件中的学生次序显示上
线的学生姓名（每行显示一个学生）

以下有四种写法供参考，使用其中一种，记得把其他方案的代码注释掉（每句代码前加"#"!)
"""

# 方案1: readlines+推导式方法，读取txt文件，将姓名成绩转成字典再输出打印
# file = open('exp09/stud.txt', mode='r')
# lines = file.readlines()
# lines = [item.strip('\n').split(',') for item in lines]
# stud = {name: int(score) for name, score in lines}
# for name, score in stud.items():
#     if score >= 305:
#         print(name)
# file.close()

# 方案2: readlines+推导式方法，读取txt文件，将姓名成绩转成列表即可输出打印
# file = open('exp09/stud.txt', mode='r')
# lines = file.readlines()
# lines = [item.replace('\n', '').split(',') for item in lines]
# for items in lines:
#     if int(items[1]) >= 305:
#         print(items[0])
# file.close()

# 方案3: readline的写法，读取txt文件，将姓名成绩转成字典再输出打印
# file = open('exp09/stud.txt', mode='r')
# while True:
#     line = file.readline()
#     if not line:
#         break
#     line = line.strip('\n').split(',')
#     if int(line[1]) >= 305:
#         print(line[0])
# file.close()

# 方案4: 直接遍历文本对象
file = open('exp09/stud.txt', mode='r')
for line in file:
    line = line.strip('\n').split(',')
    if int(line[1]) >= 305:
        print(line[0])
file.close()