import random

tests_list = ["test_login", "test_logout", "test_registration", "test_profile", "test_payment", "test_search"]
status_list = ["PASS", "FAIL", "SKIP"]

def result_tests(tests, status):
    quantity = int(input("Введите количество тестов: "))
    if quantity > len(tests):
        print("Ошибка запуска")
    else:
        selected_test = random.sample(tests, quantity)
        selected_status = [random.choice(status) for i in range(quantity)]

        report = dict(zip(selected_test, selected_status))

        for test_name, status_name in report.items():
            print(f"{test_name} — {status_name}")


result_tests(tests_list, status_list)
