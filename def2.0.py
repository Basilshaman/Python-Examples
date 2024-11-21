list1=[89,97,96,56,45,56,67,78,34,45,34,24,26,46,54,7]
g=0
while g<len(list1):
    if (list1[g])>24:
        print("passed",(list1[g]))
    g=g+1

def pattern(list1):
    g=0
    while g<len(list1):
        if (list1[g])>24:
            print("passed",(list1[g]))
        g=g+1
pattern(list1)
mark=[90,91,90,56,45,23,45,21,43,20,18]
pattern(mark)

mix=[27,48,36,327,54,36,3,63653,55,547,5,4,55,56,56,556,565,5665,34565,768766545467,6976]
def odd():
    list1=[]
    for i in mix:
        if i%2==1:
            list1.append(i)
    return(list1)
odd()
find=odd()
find

def patt(c):

    for  row in range(0,c):
        for space in range(c-row):
            print(' ',end='')
        for star in range(0,row):
         print('* ',end="")
        print(' ')
patt(20)

mix=[27,48,36,327,54,36,3,63653,55,547,5,4,55,56,56,556,565,5665,34565,768766545467,6976]

sum2=0
letter=0
while letter<len(mix):
    if mix[letter]%2==1:
        sum2=sum2+mix[letter]
    letter=letter+1
    print(sum2)
mix=[27,48,36,327,54,36,3,63653,55,547,5,4,55,56,56,556,565,5665,34565,768766545467,6976]
sum2=0
for i in mix:
    if i%2==1:
        sum2=sum2+i
print(sum2)

def pyramid(f):
    for row in range(1,f):
        for space in range(f-row):
            print(' ',end="")
        for star in range(0,row):
            print("* ",end="")
        print(' ')
pyramid(47)
def pyra(f):
    for row in range(0,f):
        for space in range(f-row):
            print(" ",end="")
        for star in range(0,row):
            print('/ ',end="")
        print('')
pyra(17)

def zero():
    list2=[]
    b=input('enter a value and <5 for quit')
    while b<'5':
        print(b)
        list2.append(b)
        b=input('enter a value and <5 for quit')
    print(list2)
zero()

def higer(x,y):
    if x>y:
        return x
    else:
        return y
higer(38,89)

def low(x,y,z):
    if x>y and x>z:
        return x
    elif y>z and x<y:
        return y 
    else:
        return z

low(100,2736,374)
low(23442,54254,45452433)
low(5321985,25675,4766432)

def low(x,y,z):
    if x>y or x>z:
        return x
    elif y>z or x>y:
        return y 
    else:
        return z
