class Account:
    def __init__(self,account_number,account_name,balance):
        self.account_number = account_number
        self.account_name = account_name
        self.balance = balance

    def get_balance(self):
        print('the current balance is', self.balance)

    def display(self):
        print('account number : ', self.account_number)
        print('account name : ', self.account_name)
        print('account balance : ', self.balance)

    def deposit(self,amount):
        self.balance = self.balance + amount


        

account1 = Account('00111222333','python_files',100)





account1.get_balance()
account1.display()
account1.deposit(100)
account1.get_balance()

    