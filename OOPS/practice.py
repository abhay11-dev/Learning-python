class Bank:
    def __init__(self,amount,account):
        self.amount = amount
        self.account = account

    def credit(self,amount):
        self.amount += amount
        print(f"Credited {amount}. New balance: {self.amount}")

    def debit(self,amount):
        if amount > self.amount:
            print("Insufficient funds")
        else:
            self.amount -= amount
            print(f"Debited {amount}. New balance: {self.amount}")
    
    def balance(self):
        print(f"Current balance: {self.amount}")



b1 = Bank(1000,"123456789")
b1.credit(500)
b1.debit(200)
b1.balance()

del b1
print("Bank account deleted")
print(b1)  # This will raise an error since b1 has been deleted