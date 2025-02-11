class Bank:
    min_balance = 2000
    bank_name = 'SBI'

    def customerdetails(self, id, fname, lname):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.total_balance = Bank.min_balance

    def deposit(self, amount):
        self.amount = amount
        self.total_balance += self.amount
        print("Customer ID:", self.id, "\nFirst name:", self.fname, "\nLast name:", self.lname, "\nBank name:",
              Bank.bank_name)
        print(self.amount, "has been credited")
        print("Balance:", self.total_balance)

    def withdraw(self, amount):
        self.amount = amount
        if self.total_balance<self.amount:
            print("Insufficient Balance")
        else:
            self.total_balance -= self.amount
            print(self.amount, "has been debited")
            print("Balance:", self.total_balance)


customer1 = Bank()
customer1.customerdetails(101, 'Varun', 'K')
customer1.deposit(20000)
customer1.withdraw(30000)
customer1.withdraw(20000)
