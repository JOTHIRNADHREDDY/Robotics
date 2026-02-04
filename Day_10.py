#Bank Account Program
class Bank_Acount():
    def __init__(self, name, account_number, balance, mobile_number):
       self.name = name
       self.__account_number = account_number
       self.balance = balance
       self.mobile_number = mobile_number

    def display_name(self):
        print("Account holder name is:", self.name)
    
    def display_account_number(self,number):
        self.__account_number = number
        print("Account number is:", self.__account_number)

    def add_balance(self, amount):
        self.balance += amount
        print("Amount added and New balance is:", self.balance)

    def check_balance(self):
        print("The balance is:", self.balance)

    def update_mobile_number(self, old_number, new_number):
        if old_number == self.mobile_number:
            self.mobile_number = new_number
            print("Mobile number updated to:", self.mobile_number)

account = Bank_Acount("Jothi", "123456789", 1000, "9515012345" )
account.display_name()
account.display_account_number("123456789")
account.add_balance(500)
account.update_mobile_number("9515012345", "9515067890")