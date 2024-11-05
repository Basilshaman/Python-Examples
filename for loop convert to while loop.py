for  row in range(1,7):
    for space in range(0,7-row):
        print(' ',end='')
    for star in range(0,row):
        print('A',end="B")
    print()
row=1
while row<7:
    space=0
    while space<(7-row):
        print(' ',end="")
        space=space+1
    star=0
    while star<row:
        print("A",end='B')
        star=star+1
    print()
    row=row+1
for  row in range(1,9,2):
    for space in range(9,row,-2):
        print(' ',end='')
    for star in range(1,row+1):
        print(star,end="")
    print("")
row=1
while row<9:
    space=9
    while space>row:
        print(' ',end="")
        space=space-2
    star=1
    while star<row+1:
        print(star,end='')
        star=star+1
    print()
    row=row+2
for  row in range(7,-1,-1):
    for space in range(7-row):
        print(' ',end='')
    for star in range(0,row):
        print('* ',end="")
    print(' ')
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
