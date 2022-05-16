from db2 import CustomerRepository
from customer import Customer

class Bank:
    def __init__(self,bankName:str)->None:
        self.__bankName = bankName
        self.__customers:list[Customer] = []
        self.__db = CustomerRepository()

    @property
    def bankName(self):
        return self.__bankName
        
    @property
    def customers(self):
        return self.__customers

    def createAccount(self, customer):
        self.__customers.append(customer)

    def displayCustomers(self):
        for customer in self.__customers:
            customer.display()
            print()

    def displayAccount(self,accountNumber: int):
        for a in self.__customers:
            if a.accountNo== accountNumber:
                a.display()
    
    def changeInfo(self,accountNumber2):
        for i in self.__customers:
            if i.accountNo == accountNumber2:
                i.fname = input("New first name:")
                i.lname = input("New last name: ")
                i.accountBalance = int(input("New account balanace: "))
            i.display()

    def printAscendingOrder(self):
        accNumList =[]
        for i in self.__customers:
            accNumList.append(int(i.accountNo))
        accNumList.sort()
        for i in accNumList:
            Bank.displayAccount(self, i)
        print()

    def printDescendingOrder(self):
        accNumList2 = []
        for i in self.__customers:
            accNumList2.append(int(i.accountNo))
        accNumList2.sort()
        accNumList2.reverse()
        for j in accNumList2:
            Bank.displayAccount(self,j)
        print() 
    
    def biggestBalance(self):
        max = 0
        for i in self.__customers:
            if i.accountBalance > max:
                max = i.accountBalance
        return max

    def smallestBalance(self):
        min = 0
        for j in self.__customers:
            if j.accountBalance< min:
                min = j.accountBalance
        return min    

    def readCustomers(self):
        self.__customers = self.__db.getCustomers()

    def writeCustomers(self):
        self.__db.writeCustomers(self.__customers)

def main():

    c1 = Customer("Barrack","Obama", 999,100000)
    c2 = Customer("Joe", "Biden", 888, 200000)
    c3 = Customer("Donald", "Trump", 777, 15000)

    bank = Bank("NPU")
    bank.readCustomers()    # get customers from the file
    bank.createAccount(c1)
    bank.createAccount(c2)
    bank.createAccount(c3)

    bank.displayCustomers()

    bank.writeCustomers()
    print("The ascending order as following: ")
    bank.printAscendingOrder()
    print("The descending order as following: ")
    bank.printDescendingOrder()
    print("The biggest balance: ")
    print(bank.biggestBalance())
    print("The smallest balance: ")
    print(bank.smallestBalance())
    bank.changeInfo(123)

    

if __name__=="__main__":
    main()