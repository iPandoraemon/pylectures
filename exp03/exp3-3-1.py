x = float(input("x="))
if x < 1:
    y = x
elif x < 10:
    y = x-1
else:
    y = 3*x-11
print("y=%.2f"%y)
