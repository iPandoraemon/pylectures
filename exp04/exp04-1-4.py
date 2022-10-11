# 1（4）输入整数n，输出以下数字三角形(每位数占3列宽度，左对齐)
n=eval(input("n:"))
for i in range(1, n+1):         # 控制行数，共n行
    for j in range(1, i+1):     # 循环输出第i行上的每一个数
        print("%-3d"%j,end="")  # 输出第j个整数(第i行上)
    print()                     # 第i行结束时换行
