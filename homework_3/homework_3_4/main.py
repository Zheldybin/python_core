import test_data


def get_count():
    count = int(input("Введите количество пользователей: "))
    return count


def print_users(users):
    for user in users:
        print(f"Пользователь: {user['login']}, Возраст: {user['age']}, Статус: {user['status']}")


def print_statistics(users):
    stats = {"ACTIVE": 0, "BLOCKED": 0, "INACTIVE": 0}
    for user in users:
        if user["status"] in stats:
            stats[user["status"]] += 1

    total = len(users)

    for status, count in stats.items():
        percent = (count / total * 100)
        print(f"Статус: {status}, Количество: {count}")


def main():
    count = get_count()

    users = [test_data.generate_user() for i in range(count)]

    print_users(users)
    print_statistics(users)



main()