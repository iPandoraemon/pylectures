"""
已知图书信息文件 (book.txt) 内分行记录图书书名和价格。

试显示书名中含有love的 (注: 书名的首字母大写) 所有书名及价格.

My  love is in heart   20.5
Sun is source of love  38.0
We love our homeland   10.5
Love is great          10.9

以下有两种写法供参考，使用其中一种，记得把另一种方案的代码注释掉（每句代码前加"#"!)
"""
# 方案1: 课本例子类似的写法
# file = open('exp09/books.txt', mode='r')
# while True:
#     line = file.readline()
#     if not line:
#         break
#     if 'love' in line.lower():
#         print(line.replace('\n', ''))
# file.close()

# 方案2: 推导式法
file = open('exp09/books.txt', mode='r')
lines = [item for item in file.readlines() if 'love' in item.lower()]
for item in lines:
    print(item.strip('\n'))
file.close()
