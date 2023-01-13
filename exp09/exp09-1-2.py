"""
输入整数n，然后再分n行输入n个学生的姓名和总分成绩(用逗号,作为分隔符),
将这些信息写入文件student.txt, 程序运行效果如下:

n=4
Mary,280
Kate,300
Rose,350
Jack,320
"""

n=int(input("n="))
stud=[]
for i in range(0,n): # range(n)
    line=input()
    stud.append(line+"\n")
file2=open("student.txt",mode='w')
file2.writelines(stud)
file2.close()
