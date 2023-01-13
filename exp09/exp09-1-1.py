"""
读取文本文件poem.txt,并将其内容分行显示出来，要求每行前面插入相应的行号
"""

# 采用“相对路径”打开文件，要确定编译器当前路径所在，即终端当前路径。
# 在终端中，输入pwd命令显示当前路径
file1=open('exp09/poem.txt', mode='r')
i=0
for line in file1:
    i=i+1
    print(str(i)+":"+line,end="")
file1.close()
