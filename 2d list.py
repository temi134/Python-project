number = [[1,2,4,5,],
          [4,5,6,12],
          [7,8,9,10]]

'''for row in number:
    for num in row:
        print(num,end= ' ')
    print()'''
'''for i in range(0,3):
    for j in range(0,3):
        print(number[i][j],end = ' ') 
    print()'''

for i in range(3):
    print(number[i][i])

for row in number:
    print(row[0])
