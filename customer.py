class Customer:
    def __init__(self,fname:str,lname:str,accountNo:int,accountBalance:float):
        self.__fname = fname
        self.__lname = lname
        self.__accountNo = accountNo
        self. __accountBalance = accountBalance

    @property
    def fname(self):
        return self.__fname
    @fname.setter
    def fname(self,fname):
        self.__fname = fname
    @property
    def lname(self):
        return self.__lname
    @lname.setter
    def lname(self,lname):
        self.__lname= lname
    @property
    def accountNo(self):
        return self.__accountNo

    @property
    def accountBalance(self):
        return self.__accountBalance

    @accountBalance.setter
    def accountBalance(self,accountBalance):
        self.__accountBalance = accountBalance

    def display(self):
        print("Client:")
        print("Firstname: ", self.__fname)
        print("Lastname: ", self.__lname)
        print("Account number.: ", self.__accountNo)
        print("Balance: ", self.__accountBalance)
