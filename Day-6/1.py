class Bank:
    def __init__(self,ownerName,Balance):
        self.ownerName=ownerName
        self.Balance=Balance
    def __str__(self):
        return "Account owner:{ownerName}\nAccount balance:${Balance}".format(ownerName=self.ownerName,Balance=self.Balance)
    
    def deposit(self,dp_money):
        self.Balance+=dp_money
        print("Deposit Accepted,you balance is {Balance}".format(Balance=self.Balance))


    def withdraw(self,wd_money):
        if wd_money > self.Balance:
            print('Funds Unavailable!')
        else:
            self.Balance -= wd_money
            print('Withdrawal Accepted, your balance is {Balance}'.format(Balance=self.Balance))

B=Bank("Ayush",500)
print(B)

B.deposit(100)
B.withdraw(125)
B.withdraw(200)
        
