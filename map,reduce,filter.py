#map
#1
def cube(i):
    return i+3
print(list(map(cube,[3,463,564,545357,73,753,75,77,])))


#2 
print(list(map(lambda n:n**3,[1,2,3,4])))

#example
#1capital letter

def cap(A):
    return A.upper()
print(list(map(cap ,('FTYGHFghfgghNBfvJHjJVgvgvJH'))))
#2
print(list(map(lambda A:A.upper(),"hfdjhjkfhdskDSDFGljklfsdj")))

#1small
def small(a):
    return a.lower()
print(list(map(small ,('FTYGHFghfgghNBfvJHjJVgvgvJH'))))
#
print(list(map(lambda a:a.lower (),('FTYGHFghfgghNBfvJHjJVgvgvJH'))))

#reduce
#1
from functools import reduce
def fun(n,f):
    return n*f
print(reduce(fun,[1,2,3,4]))

#2
from functools import reduce
print(reduce(lambda n,f:n*f,[1,2,54,5666]))

#filter
#1
def sep(n):
    return n.isalpha()
print(list(filter(sep,('ggguy7ddfs6duycx8djd87dnbddsnd7767667666'))))
#2
print(list(filter(lambda n:n.isalpha(),('fds67VFD6DF56FDv'))))