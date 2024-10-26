for symbel in range(0,7):
    print(' '*(7-symbel),symbel*' * ')
    group=[1,2.7,2+2j,'rafhina',None,False]
    type(group)
    for paste in group:
        print(paste)
    for symbel in range(0,6):
        print(group[symbel])
for value in range(0,len(group)):
    print(group[value])
for row in range(0,7):
    for col in range(0,3):
        print('*',end="")
    print('')
for row in range(0,7):
    for col in range(0,row):
        print('*',end="")
    print('')
for row in range(7,-1,-1):
    for col in range(0,row):
        print('*',end="")
    print('')
for row in range(7,-1,-1):
    for col in range(0,row):
        print(row,end="")
    print('')
for row in range(0,7):
    for col in range(0,row):
        print(row,end="")
    print('')
    print(col,end="")
    print('')
for row in range(1,7):
    for col in range(1,row):
        print(col,end="")
    print('')
for row in range(0,6):
    for col in range(0,1):
        print('5'*row)
for row in range(0,6):
    for col in range(0,1):
        print('5'*row)   
    print("#"* row)
for row in range(0,6):
    for col in range(0,1):
        print('5'*row)
    print('$'*row)
for row in range(0,7):
    for space in range(row,7):
        print(" ",end=" ")
    for star in range(0,row):
        print(" * ",end=" ")
    print("")    
for row in range(0,7):
    for space in range(row,7):
        print(" ",end=" ")
    for star in range(0,row):
        print("* ",end=" ")
    print("")
print(""*"*")
for row in range(0,7):
    for space in range(row,7):
        print(" ",end=" ")
    for star in range(0,row):
        print(" * ",end="*")
    print(" * ")
  