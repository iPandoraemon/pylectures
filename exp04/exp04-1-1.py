# 1（1）输入正整数n，求[1,n]区间内能被3或5整除的数的个数
g=0
i=1
n=int(input("n="))
while (i<=n):
  if i%3==0 or i%5==0:
    g=g+1
  i+=1
print("个数="+str(g))
