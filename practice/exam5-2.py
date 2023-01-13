import random

x=[random.randint(1,300) for i in range(200)]
r = dict()
for i in x:
    r[i] = r.get(i, 0)+1
for key, value in r.items():
    print(key, value)