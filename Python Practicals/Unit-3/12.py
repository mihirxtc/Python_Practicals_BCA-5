# 12. Write a program to implement single inheritance in which two sub classes are derived from a single base class.

class Bank(object): # object is superclass for Bank class also.
    cash = 1000000
    @classmethod
    def chk_cash(cls): # prints available cash
        print(cls.cash)

class Andhrabank(Bank): #first subclass
    pass

class Statebank(Bank): #second subclass
    cash = 200000
    @classmethod
    def chk_cash(cls):
        print(cls.cash+Bank.cash)

a = Andhrabank()
a.chk_cash()
s = Statebank()
s.chk_cash()