class Account:
    def __init__(self, bal, acc ):
        self.balance = bal
        self.accountNo = acc

    def credit(self, money):
        self.balance += money
    
    def debit(self, money):
        self.balance -= money

account1 = Account(10000,12345)
print("This is your current balance: ",account1.balance)

account1.credit(10)
print("Balance after credit: ",account1.balance)

account1.debit(10000)
print("Balance after debit: ",account1.balance)