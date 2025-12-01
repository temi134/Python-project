shopping_list = {'pencil':0.3,'rubber':0.6,'ruler':1.2,'pen':1.6}
cart = {}

for key,value in shopping_list.items():
    print(key,value)

while True:
    bought = input('what do you want to buy')

    if bought == 'stop':
        break

    if bought not in shopping_list:
        print('that item isnt present')
        continue

    else:
        quantity = int(input('how much do you want to buy'))

        cart[bought] = quantity

        print(cart)



total = 0

for keys in cart:
    amount = cart[keys]*shopping_list[keys]
    print(keys, cart[keys], shopping_list[keys],amount )
    total = total + amount

print('Your total price is', total) 


    
