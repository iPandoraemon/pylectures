'''
文本加密。输入一行字符, 试按照以下加密规则对其加密后输出其密文形式
(加密规则:字母A-Z,B-Y,C-X....a-z,b-y,c-x...,数字0-9,1-8,2-7...其他字符保持不变),
程序运行效果如下。

提示: 由于ord("A")+ord("Z")=ord("B")+ord("Y")=...=155,
则大写字母x的密文形式应该为chr(155-ord(x))

输入一行字符:123,Up,I Love you China!
加密后的密文:876,Fk,R Olev blf Xsrmz!
'''
import string

line = input("输入一行字符:")
encrypted = []      # 创建一个__列表__用来保存加密后的字符

# ---------------------------------------------------------
# 按题干提示的加密写法：
for s in line:
    # 总数-字符的编号=加密字符的编号
    if s.isdigit():
        encrypted.append(chr(105-ord(s)))   # ord('0')+ord('9')=ord('1')+ord('8')=105
    elif s.isupper():
        encrypted.append(chr(155-ord(s)))   # ord('A')+ord('Z')=155
    elif s.islower():
        encrypted.append(chr(219-ord(s)))   # ord('a')+ord('z')=219
    else:
        encrypted.append(s)                 # 其他字符
# 以上为加密过程
# ---------------------------------------------------------


# ---------------------------------------------------------
# 另一种加密写法：
# 创建大写字母、小写字母、数字的“密码本”：实际上就是倒序
# upletter_codes = string.ascii_uppercase[::-1]
# lowletter_codes = string.ascii_lowercase[::-1]
# num_codes = string.digits[::-1]

# for s in line:
#     if s.isdigit():
#         encrypted.append(num_codes[ord(s)-48])
#     elif s.isupper():
#         encrypted.append(upletter_codes[ord(s)-65])
#     elif s.islower():
#         encrypted.append(lowletter_codes[ord(s)-97])
#     else:
#         encrypted.append(s)
# 以上为加密过程
# ---------------------------------------------------------

print("加密后的密文:"+"".join(encrypted))