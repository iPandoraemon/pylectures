ck1={1:20.5,2:45.2,4:38.6,5:12.4}
ck2={2:15.8,3:60.5,4:18.7}
total = {}                      #统计后的结果字典
for k in ck1:                   #遍历仓库1中的每种材料
    if k in ck2:                #若其在仓库2中也出现
        total[k]=ck1[k]+ck2[k]  #将两个仓库中这种材料的重量之和存入统计字典
    else:                       #仅在仓库1中出现
        total[k]=ck1[k]         #将仓库1中这种材料的重量存入统计字典
for k in ck2:                   #遍历仓库2中的每种材料
    if k not in ck1:            #若其未在仓库1中也出现
        total[k]=ck2[k]         #将仓库2中这种材料的重量存入统计字典
totallist=sorted(total.items())
print("两个仓库稀土材料库存总量如下:")
for cl in totallist:
    print("材料",cl[0],":",cl[1],"吨.",sep="")
