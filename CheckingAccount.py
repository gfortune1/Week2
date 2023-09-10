class CheckingAccount:
    def __init__(self, name, address, account_number, initial_balance):
        self._name = name
        self._address = address
        self._account_number = account_number
        self._balance = initial_balance
    def debit(self, amount):
        if amount > 0 and self._balance >= amount:
            self._balance -= amount
            return True
        else:
            return False
    def credit(self, amount):
        if amount > 0:
            self._balance += amount
    def get_balance(self):
        return self._balance
# Driver application
if __name__ == "__main__":
    # Create a CheckingAccount object
    account = CheckingAccount("John Doe", "123 Main St", "1234567890", 1000.0)
    # Perform debits and credits
    account.credit(500.0)
    account.debit(200.0)
    account.credit(300.0)
    # Print the balance
    print(f"Account Balance: ${account.get_balance()}")









