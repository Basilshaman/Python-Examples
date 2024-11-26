
#multiple
list1=[1,5,7,8,2,4]
squre=1
for i in list1:
    squre=squre*i
    print(squre)
#large value
list1=[1,5,7,8,2,4]
value=list1[0]
for i in list1:
    if i>value:
        value=i
print(value)
#small value
list1=[1,5,7,8,2,4]
value=list1[0]
for i in list1:
    if i<value:
        value=i
print(value)
#strings
list2=['bsil','dell','aba','cbc','dddd','q']
count=0
for i in list2:
    if len(i)>2:
        if i[0]==i[-1]:
         count=count+1
print(count)
#duplicate
list3=[1,2,3454,6,57,34,67,653,77,59388,95,736578,54686,8,6,1,2]

lis0=[]
for i in list3:
    if i not in lis0:
        lis0.append(i)

print(lis0)
