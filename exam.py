
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
#duplicate remove
list3=[1,2,3454,6,57,34,67,653,77,59388,95,736578,54686,8,6,1,2]

lis0=[]
for i in list3:
    if i not in lis0:
        lis0.append(i)

print(lis0)
#remove
list5=['red','green','white','black','pink','yellow']
list5.pop(0)
list5.pop(3)
list5
#
def function(list1):
    a=2
    for s in list1:
        if s<2:
            return False
        for i in range(2,s):
            if s%i==0:
                return False
    return True
function(list1) 
list1=[5,3,3,5,7,11,8]
function(list1)
#1 covert a group of charecters into a srting
letter=['b','a','s','i','l']
for i in letter:
    if i not in '':
      print(i,end="")
#2
letter = ['b', 'a', 's', 'i', 'l']
result =''.join(letter)
print(type(result))

# second large
list1=[1,5,7,8,2,4]
a=0
value=list1[0]
for i in list1:
    if i>value:
        value=i
print(value)
value=list1[0]
s=0
while s<len(list1):
    if list1[s]>value:
        value=list1[s]
    s=s+1
print(value)




           


