import csv
from pathlib import Path
from customer import Customer
import os,sys

class CustomerRepository:
    def __init__(self):
        self.__FILENAME = "customers.csv"

    def getCustomers(self):
        customers = []
        with open (self.__FILENAME,newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                customer =Customer(row[0],row[1],int(row[2]),float(row[3]))
                customers.append(customer)
        return customers

    def writeCustomers(self, customers:list[Customer]):
        with open(self.__FILENAME,'w',newline="") as file:
            writer = csv.writer(file)
            for v in customers:
                line = []
                line.append(v.fname)
                line.append(v.lname)
                line.append(v.accountNo)
                line.append(v.accountBalance)
                writer.writerow(line)
            
def main():
    c = CustomerRepository()
    #c.writeCustomers()
    customers = c.getCustomers()
    for v in customers:
        v.display()

    newCustomer = Customer('Peter', 'Lee', 123450, 3000)
    customers.append(newCustomer)
    c.writeCustomers(customers)

if __name__=="__main__":
    main()



