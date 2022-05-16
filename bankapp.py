from bank import Bank
from customer import Customer

class BankApp:
    def __init__(self):
        self.__bank = Bank("NPU")
        self.__bank.readCustomers()

    @property
    def bank(self):
        return self.__bank

    def showTitle(self):
        print("The Bank Application")
        print()

    def showMenu(self):
        print("MENU")
        print("account- Show all the accounts")
        print("2. Find account info from the account number.")
        print("3. View the account list forwards.")
        print("4. View the account list backwards.")
        print("5. Find the biggest balance")
        print("6. Find the smallest balance")
        print("7. Change the account info.")
        print("8. Exit")
        print()

    def showCustomers(self):
        print("Customers")
        lineFormat1 = "{:<5s} {:<25s} {:>25s} {:>10s}"
        lineFormat2 = "{:<5s} {:<25s} {:>25d} {:>10.2f}"
        print(lineFormat1.format("Firstname","Lastname","A/C No.", "Account Balance"))
        customers = self.__bank.customers
        for customer in customers:
            print(lineFormat2.format(customer.fname,
                                     customer.lname,
                                     customer.accountNo,
                                     customer.accountBalance))
        print()

    def createNewCustomer(self, customer):
        return self.__bank.createAccount(customer)
    def showCustomer(self,accountNumber):
        return self.__bank.displayAccount(accountNumber)  

    def printForward(self):
        return self.__bank.printAscendingOrder()
    
    def printBackward(self):
        return self.__bank.printDescendingOrder()

    def searchCustomer(self,accountNumber):
        return self.__bank.displayAccount(accountNumber)

    def changeInfo(self, accountNumber2):
        return self.__bank.changeInfo(accountNumber2)

    def maxBalance(self):
        return self.__bank.biggestBalance()
    
    def minBalance(self):
        return self.__bank.smallestBalance()


def main():
    app = BankApp()
    app.showTitle()
    app.showMenu()
    app.showCustomers()

    bank = app.bank
   
    while True:
        choice = input("What is your choice: ")
        if choice == "account":
            app.showCustomers()
        elif choice == "1":
    
            firstName = input("What is first name?: ")
            lastName = input("What is last name?: ")
            accountNumber = int(input("What is account number? "))
            balance = float(input("What is account balance? "))

            cus = Customer(firstName, lastName, accountNumber,balance)
            app.createNewCustomer(cus)
            app.showCustomer(accountNumber)
   
        elif choice == "2":
            AccNum = int(input("What is account number? "))
            app.showCustomer(AccNum)

        elif choice =="3":
            print(app.printForward())

        elif choice =="4":    
            print(app.printBackward())
        
        elif choice =="5":
            print(app.maxBalance())
        
        elif choice =="6":
            print(app.minBalance())

        elif choice =="7":
            AccNum2 = int(input("What is account number? "))
            app.changeInfo(AccNum2)
            print("The information of the client has changed as following:")
            app.showCustomer(AccNum2)

        elif choice =="8":
            print("Bye")
            break
        else:
            print("Not a valid command, please try again\n")

    bank.writeCustomers()    

if __name__ == "__main__":
    main()



