print("---请输入您的参赛报名信息---")
name=input("姓名:")               #显示提示，输入一个字符串数据
sex=input("性别:")
age=eval(input("年龄:"))          #显示提示，输入数据并转换为合适的类型
country=input("国家:")
item=input("参赛项目:")
print("------------END-------------\n")
print("---您的报名信息如下---")
print("姓名:"+name)
print("性别:"+sex)
print("年龄:"+str(age))            #str函数用于将数值转换成字符串
print("国家:"+country)
print("参赛项目:"+item)
print("----------------------")