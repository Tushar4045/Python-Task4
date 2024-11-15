class bankTrans:
    def deposit_bank(self, amt, currentBankBalance):
        amt = amt + currentBankBalance
        return amt
    
    def withdraw_bank(self, amt, currentBankBalance):
        amt = currentBankBalance - amt
        return amt
    
    def deposit_user(self, amt, currentUserBalance):
        amt =   amt + currentUserBalance
        return amt
    def withdraw_user(self, amt, currentUserBalance):
        amt = currentUserBalance - amt
        return amt
    
class openAccount(bankTrans):
    bankTotalMoney = 500

    def __init__(self,amt):
        self.userBankBalance = amt
        openAccount.bankTotalMoney = openAccount.bankTotalMoney + amt

    def withDrawBankUser(self, amt):
        openAccount.bankTotalMoney = self.withdraw_bank(amt, openAccount.bankTotalMoney)
        self.userBankBalance = self.withdraw_user(amt, self.userBankBalance)
        print(f'Bank Current Balance: {openAccount.bankTotalMoney}')
        print(f'user current balance: {self.userBankBalance}')
        # self.bankTotalMoney = bankCurrentBalance
        # self.userBankBalance = userCurrentBalance

    def depositBankUser(self, amt):
        openAccount.bankTotalMoney = self.deposit_bank(amt, openAccount.bankTotalMoney)
        self.userBankBalance = self.deposit_user(amt, self.userBankBalance)
        print(f'bank current balance: {self.bankTotalMoney}')
        print(f'user current balance: {self.userBankBalance}')
        # self.bankTotalMoney = bankCurrentbalance
        # self.userBankBalance = userCurrentBalance
    
if __name__=='__main__':
    user1 = openAccount(200)
    user1.depositBankUser(100)
    user1.withDrawBankUser(50)
    print(f'Bank Total Balance: {user1.bankTotalMoney}')
    print(f'user1 Total balance: {user1.userBankBalance}')

    print()
    user2 = openAccount(0)
    user2.depositBankUser(500)
    user2.withDrawBankUser(100)
    print(f'Bank Total Balance: {user2.bankTotalMoney}')
    print(f'user2 Total balance: {user2.userBankBalance}')
