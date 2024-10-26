for  row in range(0,7):
    for space in range(7-row):
        print(' ',end='')
    for star in range(0,row):
        print('*',end="*")
    print("*")
for  row in range(0,7):
    for space in range(7-row):
        print(' ',end='')
    for star in range(0,row):
        print('*',end="*")
    print("*")
    print(' '*row)
for  row in range(1,7):
    for space in range(7-row):
        print(' ',end='')
    for star in range(0,row):
        print('A',end="B")
    print('')
for  row in range(1,9,2):
    for space in range(9,row,-2):
        print(' ',end='')
    for star in range(1,row+1):
        print(star,end="")
    print("")
for  row in range(7,-1,-1):
    for space in range(7-row):
        print(' ',end='')
    for star in range(0,row):
        print('*',end="*")
    print("*")
    print(' '*row)
for  row in range(0,7):
    for space in range(7-row):
        print(' ',end=' ')
    for star in range(0,row):
        print('*  ',end=" ")
    print("*")
for  row in range(0,7):
    for space in range(7-row):
        print('',end='')
    for star in range(0,row):
        print('*  ',end=" ")
    print("*")
for  row in range(5,-1,-1):
    for space in range(5-row):
        print('',end='')
    for star in range(0,row):
        print('*  ',end=" ")
    print("*")
for  row in range(0,7):
    for space in range(7-row):
        print('',end='  ')
    for star in range(0,row):
        print('* ',end="")
    print("")
for  row in range(7,-1,-1):
    for space in range(7-row):
        print('',end='  ')
    for star in range(0,row):
        print('* ',end="")
    print("")
for  row in range(0,7):
    for space in range(7-row):
        print(' ',end=' ')
    for star in range(0,row):
        print(' * ',end=" ")
    print("")
for  row in range(7,-1,-1):
    for space in range(7-row):
        print(' ',end=' ')
    for star in range(0,row):
        print(' * ',end=" ")
    print("")
for  row in range(1,7):
    for space in range(7-row):
        print(' ',end=' ')
    for star in range(1,row):
        print(' * ',end=" ")
    print("")

