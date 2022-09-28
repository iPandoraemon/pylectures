'''多行注释第一行
多行注释第二行
多行注释第三行'''
def add(a):               # 函数定义语句
    b = eval(input(""))   # 输入语句
    c = 1                 # 赋值语句
    if b<0:
        print("Input must be bigger than 0!")
    else:
        d = a+b+c
    return d              # 函数返回语句

x = add(5)                # 调用自定义函数add()
print(x)                  # 输出变量x
