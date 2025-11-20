class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder  # Public
        self._account_number = self._generate_account_number()  # Protected
        self.__balance = initial_balance  # Private (name mangled)

    def _generate_account_number(self):
        """Protected method - for internal use"""
        import random
        return f"ACC{random.randint(10000, 99999)}"

    def deposit(self, amount):
        """Public method - interface for users"""
        if amount > 0:
            self.__balance += amount
            self.__update_transaction_history(f"Deposit: +${amount}")
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self.__update_transaction_history(f"Withdrawal: -${amount}")
            return True
        return False

    def get_balance(self):
        """Public getter for private attribute"""
        return self.__balance

    def __update_transaction_history(self, transaction):
        """Private method - internal implementation"""
        # In real implementation, this would update a database or file
        print(f"Transaction recorded: {transaction}")

# Using the encapsulated class
account = BankAccount("Alice", 1000)

print(account.account_holder)     # Alice (public - accessible)
print(account._account_number)    # ACC12345 (protected - accessible but shouldn't be)
# print(account.__balance)        # Error! Private attribute

account.deposit(500)              # Transaction recorded: Deposit: +$500
account.withdraw(200)             # Transaction recorded: Withdrawal: -$200
print(account.get_balance())      # 1300 (using public getter)
