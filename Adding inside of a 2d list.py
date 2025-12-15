List_1 = [[1,2,3,4,5],
         [6,7,8,9,10],
         [11,12,13,14,15]]

List_2 = [0,0,0]

amount = 0

for i in range(3):
    for j in range(5):
        amount = List_1[i][j] + amount
        print(amount)
    List_2[i] = amount
    amount = 0

print(List_2)