#exersice(map)
#squre of numbers

#1
def squ(n):
    return n**3
print(list(map(squ,[1,2,3,4])))
#2
print(list(map(lambda n:n**3,[1,2,3,4])))

#celsius convert to farenheit
#1
def far(n):
    return n*9/5+32
print(list(map(far,[0,20,37,100])))
#2
print(list(map(lambda n:n*9/5+32,[0,20,37,100])))

#string length
#1
def num(n):
    return len(n)
print(list(map(num,['apple','dghghgh','fttf'])))
#2
print(list(map(lambda n:len(n),['apple','dghghgh','fttf'])))

#(filter)
# sum of number
#1
def tot(n):
    return n%2==0
print(list(filter(tot,[1,2,3,4,5,6,7,8,9]))) 
#2
print(list(filter(lambda n:n%2==0,[1,2,3,4,5,6,7,8,9]))) 
#longerthan 5 letter
#1
def hig(n):
    return len(n)>=5
print(list(filter(hig,['banana','apple','cat','dog','elephant'])))
#2
print(list(filter(lambda n:len(n)>=5,['banana','apple','cat','dog','elephant'])))
#palindrome
#1
def pal(n):
    return True if n[0::]==n[::-1]else False
print(list(filter(pal,['banana','cardrac','madam','world','hello'])))
#2
print(list(filter(lambda n:True if n[0::]==n[::-1]else False,['banana','cardrac','madam','world','hello'])))
#(reduce)
#sum
#1
from functools import reduce
def sum(n,y):
    return n+y
print(reduce(sum,[1,2,3,4,5]))
#2
print(reduce(lambda n,y:n+y,[1,2,3,4,5]))
#max
#1 
def max(n,y):
    return n if n>y else y
print(reduce(max,[5,1,8,3,7,9,2]))
#2
print(reduce(lambda n,y:n if n>y else y,[5,1,8,3,7,9,2]))
#multi(product  of number)
#1
def max(n,y):
    return n * y
print(reduce(max,[4,1,3,2]))
#2
print(reduce(lambda n,y:n*y,[4,1,3,2]))
#(combine)
def sqr(n):
    return n**2
a=list(map(lambda n:n**2,[1,5,10,7,8]))
print(list(filter(lambda n:True if n>50 else False,a)))
