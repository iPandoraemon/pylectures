'''
分多行输入好友通讯录信息（每位好友的姓名和电话号码），输入一个好友的姓名，
快速显示出他(她)的电话号码，若姓名不存在，则显示查无此人。

输入好友的信息(姓名:电话):
Rose:13307343189
Jack:15102011521
Peter:15020200001
July:39352075
Geery:13901013456
#
姓名:July
电话:39352075
'''
contacts = {}

print("输入好友的信息(姓名:电话):")
while True:
    line = input()
    if line == '#':
        break
    l_line = line.split(sep=':')
    contacts.setdefault(l_line[0], l_line[1])

name = input("姓名:")
print("电话:%s"%contacts.get(name, "没有"+name+"的电话！"))
