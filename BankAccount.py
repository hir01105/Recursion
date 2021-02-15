import math, random
class BankAccount:
    interestPerDay = 0.0001
    def __init__(self, bankName, ownerName, savings, interestPerDay):
        self.bankName = bankName
        self.ownerName = ownerName
        self.savings = savings
        self.interestPerDay = interestPerDay

    def showInfo(self):
        print("bank: {}\nowner name: {}\nbank account number: {}\nsavings: {}\nInterest rate: {}".format(self.bankName, self.ownerName, self.getRandomInteger(), self.savings, self.interestPerDay))

        
    def getRandomInteger(self):
        num = str(random.randint(1, 100000000))
        return num.zfill(9)

    def depositMoney(self, depositAmount):
        if self.savings <= 20000:
            depositAmount -= 100
        
        self.savings += depositAmount
        print(int(self.savings))
        return int(self.savings)

    def withdrawMoney(self, withdrawAmount):
        if withdrawAmount <= self.savings * 0.2:
            self.savings -= withdrawAmount
            print(int(withdrawAmount))
            return int(withdrawAmount)
        else:
            withdrawAmount = self.savings * 0.2
            self.savings -= withdrawAmount
            print(int(withdrawAmount))
            return int(withdrawAmount)


    def pastime(self, days):
        for day in range(0, days):
            self.savings = self.savings * (1 + self.interestPerDay)
        print(self.savings)
        return self.savings

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
user1BankAccount = BankAccount("Chase", user1.name, 30000, 0.010001)
user1BankAccount.showInfo()
user1BankAccount.withdrawMoney(1000)
user1BankAccount.depositMoney(10000)
user1BankAccount.pastime(200)
# Bank Of America
# Remy Clay
# 10000
# 0.010001
user2 = User("Remy", "Clay", 35, "Male")
user2BankAccount = BankAccount("Bank of America", user2.name, 10000, 0.010001)
user2BankAccount.showInfo()
user2BankAccount.withdrawMoney(5000)
user2BankAccount.depositMoney(12000)
user2BankAccount.pastime(500)