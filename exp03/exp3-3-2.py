month = int(input("输入月份: "))
if 2 <= month <= 4:
    print("春天")
elif 5 <= month <= 7:
    print("夏天")
elif month in [8, 9, 10]:
    print("秋天")
elif month in [11, 12, 1]:
    print("冬天")
else:
    print("月份错误")