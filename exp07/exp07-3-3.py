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

upletter_codes = string.ascii_uppercase[::-1]
lowletter_codes = string.ascii_lowercase[::-1]
num_codes = string.digits[::-1]

l_encrypted = []
for s in line:
    if s.isdigit():
        l_encrypted.append(num_codes[ord(s)-48])
    elif s.isupper():
        l_encrypted.append(upletter_codes[ord(s)-65])
    elif s.islower():
        l_encrypted.append(lowletter_codes[ord(s)-97])
    else:
        l_encrypted.append(s)

print("加密后的密文:"+"".join(l_encrypted))