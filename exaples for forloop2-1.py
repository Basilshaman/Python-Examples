for row in range(1,9):
    for space in range(row-9):
        print(' ',end="")
    for star in range(row,9):
        print(row,end="")
    print('')
for row in range(1,9):
    for space in range(9-row):
        print(' ',end=" ")
    for star in range(0,row):
        print(" * ",end=" ")
    print('')
for row in range(0,5):
    for space in range(row-5):
        print('',end="")
    for star in range(0,5):
        print(row,end="")
    print('')
for row in range(0,7):
    print(' '*(7-row)+' / '*row)
for row in range(1,9):
    for space in range(9-row):
        print('',end="")
    for star in range(0,row):
        print(" / ",end=" ")
    print('')
for row in range(9,-1,-1):
    for space in range(9-row):
        print('',end="")
    for star in range(0,row):
        print(" / ",end=" ")
    print('')
for row in range(0,5):
    print(1,row+1)
value=7
for row in range(1,value+1):
    for star in range(1,value+1):
        if star<=row:
           print(row,  end=" ")
        else:
          print(star, end=" ")
    print('')
for row in range(1,value+1):
    print(row)
for row in range(1,7):
    for star in range(1,7):
        if star<row:
           print(row,  end=" ")
        else:
          print(star, end=" ")
    print('')
for row in range(0,9):
    for space in range(9-row):
        print('*',end="")
    for star in range(0,row):
        print("_",end="")
    print('')
