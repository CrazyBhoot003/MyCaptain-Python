list = [0,1]

a = 0
i=0
while i<11: 
    a = list[-1] + list[-2]
    list.append(a)
    i+=1
print(list)