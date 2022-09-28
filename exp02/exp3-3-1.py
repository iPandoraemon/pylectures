"""
输入体检人的身高与体重，编程求解其体重指数BMI值，保留两位小数

体重:65
身高:1.62
BMI=体重/身高的平方(国际单位kg/㎡)
BMI=24.77
"""
weight=float(input("体重(kg):"))
height=float(input("身高(米):"))
print("BMI= %5.2f"%(weight/height**2))