#sum 
lis1=[8,2,3,0,7]
sum=0
for i in lis1:
    sum=sum+i
print(sum)

#multiply
lis2=[8,2,3,-1,7]
multi=1
for i in lis2:
    multi=i*multi
    print(multi)

#number of lower&upper
string='The quick Brow Fox'
cap=0
smal=0
for i  in string:
   if i.isupper():
       cap=cap+1
   else:
       smal=smal+1
cap
smal
#remove dublicate
lis3=[1,2,3,3,3,3,4,5]
og=[]
for i in lis3:
    if i not in og:
        og.append(i)
print(og)
#alphabetic order
lis4=['green','black','red','yellow']
alpha=sorted(lis4)
print(alpha)

# 1period

def period1(lis5):
   for i in lis5:
    if 10<i<20:
        return True
   return False

lis5=[21,50,76]
period1(lis5)
lis1

period1(lis1)
lis9=[15,16,17]
period1(lis9)

#prime or not
def prime(i):
    
    if i<2:
        return ('no')
    for s in range(2,i):
        if i%s==0:
          return ('no')
    return ('yes')

prime(i)
i=9
s=5
prime(s)

#perfect or not

1,2,3
def perfcet(a):
    if a<1:
        return ('no')
    per=0
    for s in range(1,a):
        if a%s==0:
            per=per+s
    return ('yes') if per==a else 'no'
a=6
prime(a)

