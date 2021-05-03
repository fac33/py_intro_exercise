################################################################################
# Author:Fanyang Cheng
# Date:13/04/2021
# Description: This program mimic a user's bank account which has the method
#deposit, withdraw and get_balance (show the amount). And also there would be
# an attribute called balance which record the amount of money in the account.And
#also, there will be a child class called savings which could count for the account's
#interest and add them to balance.
################################################################################
#define the class Account.
class Account:
    def __init__(self,balance):
        self.balance = balance
        #print the balance when instantiation.
        print('New account balance: $',format(self.balance,'.2f'),sep = '')
    #then is the deposit,withdraw,get_balance functions
    def deposit(self,amount):
        self.balance = self.balance+amount
        print('Deposit: $',format(amount,'.2f'),sep = '')
    def withdraw(self,amount):
        print('Withdraw: $',format(amount,'.2f'),sep = '')
        if self.balance >= amount:
            self.balance = self.balance-amount
        else:
            print('Insufficient funds. Withdrawal canceled.')
    def get_balance(self):
        print('Balance: $',format(self.balance,'.2f'),sep = '')
#define the savings class.
class Savings(Account):
    def __init__(self,balance,interest_rate):
        super().__init__(balance)
        self.interest_rate = interest_rate
    def accrue_interest(self):
        t_i = self.balance*self.interest_rate
        self.balance = self.balance+t_i
        print('Interest payment: $',format(t_i,'.2f'),sep = '')

def main():
    #set saving accounts
    save = Savings(200,0.1)
    save.get_balance()
    save.deposit(12.34)
    save.get_balance()
    save.withdraw(40.00)
    save.get_balance()
    save.withdraw(200.00)
    save.get_balance()
    save.accrue_interest()
    save.accrue_interest()
    save.accrue_interest()
    save.withdraw(200.00)
    save.get_balance()



if __name__ == '__main__':
    main()
