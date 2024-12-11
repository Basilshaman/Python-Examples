#lamda
total=lambda n: n+1
print(total(5))

total=lambda n,d: n+d+1
print(total(5,6))

total=lambda n,d: n*d+1
print(total(5,6))

total=lambda n,d: n*d+1
print('value',total(5,6))

total=lambda n: n+n*n
print(total(5)) 


#create def 
def value(i):
    if i %2==0:
        return True
    else:
        return False
value(12563856486747478)

#content
True if 5%2==0 else False

#convert if to lambda

value=lambda i:True if i%2==0 else False
print(value(667))

#cerate for loop

for i in range(1,9):
    print(i**2)

#content
[i**2 for i in range(1,9)]

#convert for to lambda

value=lambda e:[i**2 for i in range(e)]
print(value(5))