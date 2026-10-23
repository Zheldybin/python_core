class Flower:
    def __init__(self, name, price, lifespan):
        self.name = name
        self.price = price
        self.lifespan = lifespan


class Rose(Flower):
    def __init__(self, price=150, lifespan=7):
        super().__init__("Роза", price, lifespan)


class Tulip(Flower):
    def __init__(self, price=80, lifespan=5):
        super().__init__("Тюльпан", price, lifespan)


class Chamomile(Flower):
    def __init__(self, price=50, lifespan=10):
        super().__init__("Ромашка", price, lifespan)


class Accessory:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Bouquet:
    def __init__(self):
        self.flowers = []
        self.accessories = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def add_accessory(self, accessory):
        self.accessories.append(accessory)

    def get_total_cost(self):
        flowers_cost = sum(f.price for f in self.flowers)
        acc_cost = sum(a.price for a in self.accessories)
        return flowers_cost + acc_cost

    def get_withering_time(self):
        if not self.flowers:
            return 0
        total_lifespan = sum(f.lifespan for f in self.flowers)
        return total_lifespan / len(self.flowers)

    def sort_price(self):
        self.flowers.sort(key=lambda f: f.price)

    def has_flower(self, flower_name):
        for f in self.flowers:
            if f.name.lower() == flower_name.lower():
                return True
        return False


# 1. Создаем букет
my_bouquet = Bouquet()

# 2. Собираем букет
my_bouquet.add_flower(Rose(price=250)) # Дорогая роза
my_bouquet.add_flower(Tulip())         # Тюльпан (80)
my_bouquet.add_flower(Chamomile())     # Ромашка (50)

# 3. Добавляем аксессуары
my_bouquet.add_accessory(Accessory("Упаковочная бумага", 100))

print("До сортировки")
for f in my_bouquet.flowers:
    print(f" - {f.name}: {f.price} руб.")


# 4. Сортируем по цене
my_bouquet.sort_price()

print("После сортировки")
for f in my_bouquet.flowers:
    print(f" - {f.name}: {f.price} руб.")

# 5. Проверяем наличие цветов
print("Проверяем есть ли цветок в букете")
print(f"Есть ли Роза? {my_bouquet.has_flower('Роза')}")
print(f"Есть ли Лилия? {my_bouquet.has_flower('Лилия')}")