name='paBloGavi'
count=0
for string in name:
    if string.isupper():
        count=count+1
count
for string in name:
    if string.islower():
        print(string)
ne='aljandroBALDE'
count=0
count1=0
for letter in ne:
    if letter.islower():
        count=count+1
    else:
        count1=count1+1
count
count1
list1=[]
list2=[]
for letter in ne:
    if letter.islower():
        list1.append(letter)
        count=count+1
    else:
        list2.append(letter)
        count1=count1+1
        
print(list1)
print(list2)
data='Ly19'
count=0
count1=0
count2=0
list3=[]
list4=[]
other=[]
for letter in data:
    if letter.islower():
        list3.append(letter)
        count=count+1
    elif letter.isupper():
            list4.append(letter)
            count1=count1+1
    else:
        other.append(letter)
        count2=count2+1


print(list3)
print(list4)
print(other)
count
count1
count2
evensum=0
oddsum=0
for value in range(0,51):
   if value%2==0:
        evensum=evensum+value
   else:
       oddsum=oddsum+value

evensum
oddsum
'*'*5
for name in range(1,7):
    print(name*"*")
for name in range(1,7):
    print (name*"*")
for name in range(7,0,-1):
    print (name*'*')
 
for value in range(0,6):
    print(" "*(6-value),value*" * ")
for value in range(0,10):
    print(" "*(9-value),value*" * ")
    

     

