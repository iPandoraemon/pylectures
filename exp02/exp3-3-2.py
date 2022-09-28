"""
输入三角形的三边长度, 利用海伦公式:

【设三边长为a、b、c，则面积S=(p*(p-a)*(p-b)*(p-c))**0.5，其中p=(a+b+c)*0.5)】

计算该三角形的面积（保留4位小数）
"""
a = float(input("a="))
b = float(input("b="))
c = float(input("c="))
p = (a+b+c)*0.5
S = (p*(p-a)*(p-b)*(p-c))**0.5
print("Area of the triangle: %.4f"%(S))