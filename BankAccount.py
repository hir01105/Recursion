import math, random
class BankAccount:
    self.interestPerDay = 1.0001
    def __init__(self, bankName, ownerName, savings, interestPerDay):
        self.bankName = bankName
        self.ownerName = ownerName
        self.savings = savings
        self.interestPerDay = interestPerDay

    def showInfo(self):
        return "bank: {}\nowner name: {}\nbank account number: {}\nsavings: {}\nInterest rate: {}".format(self.bankName, self.ownerName, self.getRandomInteger(), self.savings, self.interestPerDay)
        
    def getRandomInteger(self):
        num = str(random.randint(1, 100000000))
        return num.zfill(9)

    def depositMoney(self, depositAmount):
        if depositAmount <= 20000:
            depositAmount -= 100
        
        self.savings += depositAmount
        return self.savings

    def withdrawMoney(self, withdrawAmount):
        if withdrawAmount <= self.savings * 0.2:
            self.savings -= withdrawAmount
            return withdrawAmount
        else:
            return "You cannot withdraw that amount"

    def pastime(self, days):
        initSavings = self.savings
        for day in range(0, days):
            self.savings = self.savings * self.interestPerDay
        
        return self.savings - initSavings

class User:
    def __init__(self, firstName, lastName, age, sex):
        self.firstName = firstName
        self.lastName = lastName
        self.name = firstName + " " + lastName
        self.age = age
        self.sex = sex

        
# Chase
# Claire Simmons
# 30000
# 0.010001
user1 = User("Claire", "Simmons", 25, "Female")
user1BankAccount = BankAccount("Chase", user1.name, )

# Bank Of America
# Remy Clay
# 10000
# 0.010001