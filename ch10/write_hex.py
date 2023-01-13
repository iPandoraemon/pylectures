def str_2_bin(str):
    """
    字符串转换为二进制
    """
    return ' '.join([bin(ord(c)).replace('0b', '') for c in str])


f1=open("ch10/登鹳雀楼.txt", "r")
strlist = f1.readlines()
for i in range(0, len(strlist)):
    strlist[i] = str_2_bin(str(i+1)+ ' ' + strlist[i])
f1.close()

f2 = open("ch10/二进制文件.txt", 'wb')
f2.writelines(strlist)
f2.close()

