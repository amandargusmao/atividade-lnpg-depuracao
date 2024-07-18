class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.balance


class Customer:
    def __init__(self, name, customer_id):
        self.name = name
        self.customer_id = customer_id
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def get_total_balance(self):
        total_balance = 0
        for account in self.accounts:
            total_balance += account.get_balance()
        return total_balance


class Bank:
    def __init__(self, name):
        self.name = name
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def get_customer(self, customer_id):
        for customer in self.customers:
            if customer.customer_id == customer_id:
                return customer
        return None

    def transfer(self, from_account, to_account, amount):
        if from_account.get_balance() >= amount:  # Condicional adicionada com o objetivo de verificar se há saldo suficiente na conta de origem
            from_account.withdraw(amount)
            to_account.deposit(amount)
        else:
            print("Insufficient funds for transfer")  # Trecho adicionado para informar quando não houver saldo na conta


def main():

    my_bank = Bank("MyBank")

    alice = Customer("Alice", 1)
    bob = Customer("Bob", 2)

    my_bank.add_customer(alice)
    my_bank.add_customer(bob)

    alice_account = Account("A001", 1000)
    bob_account = Account("B001", 500)

    alice.add_account(alice_account)
    bob.add_account(bob_account)

    my_bank.transfer(alice_account, bob_account, 300)

    print("Alice's balance:", alice_account.get_balance())
    print("Bob's balance:", bob_account.get_balance())

if __name__ == "__main__":
    main()
