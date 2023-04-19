class Person:
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name


class Client(Person):
    def __init__(self, name, last_name, account_number, bank_balance=0):
        super().__init__(name, last_name)
        self.account_number = account_number
        self.bank_balance = bank_balance

    def __str__(self):
        return f'Client:\n{self.name} {self.last_name}\nAccount Number: {self.account_number}\nBank Balance: {self.bank_balance}'

    def deposit(self, amount_deposit):
        self.bank_balance += amount_deposit
        print('Deposit made successfully')

    def withdraw(self, amount_withdraw):
        if self.bank_balance >= amount_withdraw:
            self.bank_balance -= amount_withdraw
            print('Withdrawal made successfully')
        else:
            print('Insufficient funds')


def create_cliente():
    client_name = input('Enter your name: ')
    client_last_name = input('Enter your last name: ')
    client_account_number = int(input('Enter your bank account number: '))

    client_active = Client(client_name, client_last_name, client_account_number)
    return client_active


def start():
    my_client = create_cliente()
    print(my_client)
    option = 0

    while option != 'e':
        print('''
        - [d] Deposit
        - [w] Withdraw
        - [e] Exit
        ''')
        option = input().lower()

        if option == 'd':
            amount_to_deposit = int(input('Amount to deposit: '))
            my_client.deposit(amount_to_deposit)
        elif option == 'w':
            amount_to_withdraw = int(input('Amount to withdraw: '))
            my_client.withdraw(amount_to_withdraw)
        print(my_client)

    print('thanks')




start()
