class CreditCard:
    balance = 0
    def __init__(self, card_number, start_balance):
        self.card_number = card_number
        self.start_balance = start_balance

    def deposit(self, amount):
        self.start_balance += amount

    def withdraw(self, amount):
        if(self.start_balance - amount < 0):
            print(f"Операция по счету {self.card_number} не может быть выполнена. Баланс не может быть отрицательным!")
        else:
            self.start_balance -= amount

    def show_info(self):
        print(f'Номер счёта: {self.card_number}, Текущий баланс: {self.start_balance} ')


CardNumber_1 = CreditCard(88005553535, 2000)
CardNumber_2 = CreditCard(33202, 1000)
CardNumber_3 = CreditCard(6542358, 5000)

CardNumber_1.deposit(300)
CardNumber_2.deposit(200)
CardNumber_3.withdraw(6000)

CardNumber_1.show_info()
CardNumber_2.show_info()
CardNumber_3.show_info()