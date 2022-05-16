from db import CustomerRepository
from customer import Customer, Bank

def main():
    a = CustomerRepository()
    a.getCustomers()

    customer = Customer()
