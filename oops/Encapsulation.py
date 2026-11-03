# Protected

class Bank():
    def __init__(self):        #default constructor
        self._balance=1000

class AccountHolder(Bank):
    def show_balance(self):
        print(self._balance)


obj1= AccountHolder()
obj1.show_balance()




# Private

# class Bank():
#     def __init__(self):
#         self.__balance=1000

# class AccountHolder(Bank):
#     def show_balance(self):
#         print(self.__balance)
    


# obj1= AccountHolder()
# obj1.show_balance()



# class Bank:
#     def __init__(self):
#         self.__balance = 1000

#     def get_balance(self):
#         return self.__balance


# class AccountHolder(Bank):
#     def show_balance(self):
#         print(self.get_balance())


# obj1 = AccountHolder()
# obj1.show_balance()




# class Bank:
#     def __init__(self):
#         self.__balance = 1000

#     def get_balance(self):
#         return self.__balance


# class AccountHolder(Bank):
#     def show_balance(self):
#         print(super().get_balance())


# obj = AccountHolder()
# obj.show_balance()