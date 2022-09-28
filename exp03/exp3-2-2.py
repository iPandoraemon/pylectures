w = float(input("体重(kg): "))
h = float(input("身高(m):"))
bmi = w/(h*h)
if bmi < 18.5:
    dj = "偏瘦"
elif bmi < 24:
    dj = "正常"
elif bmi < 28:
    dj = "偏胖"
elif bmi < 30:
    dj = "肥胖"
elif bmi < 40:
    dj = "重度肥胖"
else:
    dj = "极重度肥胖"
print("评价等级:"+dj)