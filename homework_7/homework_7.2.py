class ATM:
    def __init__(self, count_100, count_50, count_20):
        self.count_100 = count_100
        self.count_50 = count_50
        self.count_20 = count_20

    def add_money(self, count_100, count_50, count_20):
        self.count_100 = self.count_100 + count_100
        self.count_50 = self.count_50 + count_50
        self.count_20 = self.count_20 + count_20

    def withdraw(self, amount):
        for give_100 in range(0, self.count_100 + 1):
            for give_50 in range(0, self.count_50 + 1):
                rest = amount - give_100 * 100 - give_50 * 50

                if rest < 0:
                    continue

                if rest % 20 != 0:
                    continue

                give_20 = rest // 20

                if give_20 > self.count_20:
                    continue

                self.count_100 = self.count_100 - give_100
                self.count_50 = self.count_50 - give_50
                self.count_20 = self.count_20 - give_20

                print("  купюр по 100:", give_100)
                print("  купюр по 50: ", give_50)
                print("  купюр по 20: ", give_20)
                return True

        print("Нельзя выдать сумму", amount)
        return False

atm = ATM(2, 3, 5)
print("Начало:", atm.count_100, atm.count_50, atm.count_20)

atm.add_money(1, 0, 10)
print("После add_money:", atm.count_100, atm.count_50, atm.count_20)

atm.withdraw(270)
print("После снятия 270:", atm.count_100, atm.count_50, atm.count_20)

atm.withdraw(110)
print("После снятия 110:", atm.count_100, atm.count_50, atm.count_20)

atm.withdraw(30)
print("После попытки снять 30:", atm.count_100, atm.count_50, atm.count_20)