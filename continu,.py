value=[1,2,3,4,56,7,8,9,0,88,756,4]
s=0
while value[s]!=0:
    print(value[s])
    s=s+1
value=[1,2,3,4,56,7,8,9,0,88,756,4]
i=0
while i<12:
    if value[i]==8:
        i=i+1
        continue    
    print(value[i])
    i=i+1
gp=[1,2,3,4,5,6,7,8,9]
d=0
while d<9:
    if gp[d]==6:
        break
    print(gp[d])
    d=d+1
price=[23,32,20,45,76,96,35,34,64,98]
value=0
while value<10:
    if (price[value])==45:
        value=value+1
        continue
    print(price[value])
    value=value+1
no=[1,2,3,4,5,6,6,7]
price=[23,32,20,45,76,96,35,34,64,98]
def sum1(x):
    
    value=0
    while value<10:
        if (x[value])==45:
            value=value+1
            continue
        print(x[value])
        value=value+1

sum1(price)
sum1(no)
def sum2(data):
    for i in range(0,len(data)):
        for space in range(7-i):
            print(' ',end='')
        for star in range(0,i+1):
            print(data[i],end=" ")
        print("")
sum2(no)
sum2(price)
g=[1,2,3,4,5,6,7,89,1,23,4,5,6,6]
for s in g:
        while s<5:
           print(s)
        
