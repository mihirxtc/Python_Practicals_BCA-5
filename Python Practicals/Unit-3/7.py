# 7. Create a Bank class with two variable name and balance. Implement a constructor to initialize the variables. Also implement deposit and withdrawals using instance methods.

import sys
class bank(object):
    def __init__(self, name, balance=0.0):
        self.name = name
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdrawals(self, amount):
        if amount > self.balance:
            print("Low Balance, Cannot withdraw")
        else:
            self.balance -= amount
        return self.balance

# creates an account with given name and balance 0.0
name = input("Enter name : ")
b = bank(name)

while(True):
    print("d/D -deposit, w/W -withdrawal, e/E -exit")
    
    choice = input("Enter your choice : ")
    if choice == "e" or choice == "E":
        sys.exit()

    amount = float(input("Enter amount : "))
    if choice == "d" or choice == "D":
        print("Balance after deposit : ", b.deposit(amount))
    
    elif choice == "w" or choice == "W":
        print("Balance after withdrawals : ", b.withdrawals(amount))
