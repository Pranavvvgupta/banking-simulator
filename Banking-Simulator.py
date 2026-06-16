class account:
    def __init__(self,bal ,acc):
        self.balance = bal
        self.account = acc

    def debit(self,amount):
        if amount >self.balance:
            print("insufficient balance")
        else:
         self.balance -= amount
         print(f"₹{amount} was debited")
         print(f"remaining balance = ₹{self.balance}")

    def credit(self,amount):
        self.balance += amount
        print(f"₹{amount} was credited")
        print(f"new balance = ₹{self.balance}")

    def remaining_balance(self):
        return self.balance
        
acc1 = account(10000,1008)
account_number = int(input("enter account number: "))

debit_credit= input("do you want to debit or credit:").lower()

amount1 = int(input(f"enter amount to be updated ₹:"))

if(account_number == acc1.account and debit_credit== "debit"):
    acc1.debit(amount1)
elif(account_number == acc1.account and debit_credit == "credit"):
    acc1.credit(amount1)
else:
    print("enter valid account number")
