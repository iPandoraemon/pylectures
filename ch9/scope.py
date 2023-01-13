n, s = 5, 10   #n, s为全局变量
def fact(n) :  #n局部变量
    s = 1      #s局部变量
    for i in range(1, n+1):
        s *= i
    return s

print(fact(n), s)
