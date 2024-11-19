value=[23,45,67,89,23,12,23,45,67,89,0]
row=0
while row<11:
    if (value[row])==67:
        row=row+1
        break
    print(value[row])
    row=row+1
def sum(value):
    row=0
    while row<11:
        if (value[row])==67:
            row=row+1
            break
        print(value[row])
        row=row+1
price=[34,56,56,47,67,90,89,6]
sum(price)
score=[30,36,38,40,57,46,56,48]
for i in score:
    if i<40:
        print("failed",i)
def sum1(score):
    for i in score:
       if i<40:
         print("failed",i)
sum1(score)
sum1(value)
list1=[23,34,56,35,76,56]
s=0
while s<len(list1):
    if list1[s]>50:
        print("passed",list1[s])
    s=s+1
row=7
while row>-1:
    space=0
    while space<(7-row):
     print(' ',end='')
     space=space+1
    star=0
    while star<row:
        print("* ",end="")
        star=star+1
    print("")
    row=row-1
mix=[27,48,36,327,54,36,3,63653,55,547,5,4,55,56,56,556,565,5665,34565,768766545467,6976]
letter=0
while letter<len(mix):
        print(mix[letter])
        letter=letter+1
       
mix=[27,48,36,327,54,36,3,63653,55,547,5,4,55,56,56,556,565,5665,34565,768766545467,6976]
sum2=0
for i in mix:
    if i%2==1:
        sum2=sum2+i
print(sum2)



mix=[27,48,36,327,54,36,3,63653,55,547,5,4,55,56,56,556,565,5665,34565,768766545467,6976]
sum2=0
letter=0
while letter<len(mix):
    if mix[letter]%2==1:
        sum2=sum2+mix[letter]
    letter=letter+1
print(sum2)

def displey(mix):
    sum2=0
    letter=0
    while letter<len(mix):
        if mix[letter]%2==1:
            sum2=sum2+mix[letter]
        letter=letter+1
    print(sum2)
displey(mix)
displey(value)
displey(list1)

    


    
        

