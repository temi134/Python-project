items = {'toys':12, 'pencil':0.4, 'rubber':0.2, 'ball':50}

print(items)

print(""" 1. View the menu 
2. Add to the menu 
3. Remove from the menu
4. Change the menu 
5. Exit""")

while True:

    choice = int(input('Choose what you want to do'))

    if choice == 1:
        for key in items:
            print(key,items[key])
            
        for key,value in items.items():
            print(key,value)
    elif choice == 2:
        print(items)
        print('What item do you want to add')
        item = input()
        print('what is the cost')
        cost = float(input())
        items[item] = cost
        print(items)

    elif choice == 3:
        print(items)
        print('what item do you want to delete')
        delete = input()
        del items[delete]
        print(items)

    elif choice == 4:
        print(items)
        print('what item do you want to change')
        change = input()
        print('what is the new value')
        price = float(input())
        items[change] = price
        print(items)

    elif choice == 5:
        break

    