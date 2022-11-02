# 以行方式输入一3*3矩阵，求该矩阵中的最大值并输出

jz=[]                                 #存放矩阵数据的空列表
for i in range(3):                    #循环输入3行数据
    jz.append(list(eval(input())))    #输入1行数据，并追加到矩阵列表
linemax=[]                            #存放每行的最大值的空列表
for i in range(3):                    #求矩阵中每行的最大值
    linemax.append(max(jz[i]))        #将第i行的最大值追加到列表linemax中
print("最大值=%d"%(max(linemax)))      #输出每行最大值中的最大值
