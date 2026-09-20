test_cases = ["Login", "Registration", "Checkout", "Logout"]
statuses = ["PASS", "FAIL", "PASS", "SKIP"]

def print_report(test_cases, statuses):
    count_pass = 0
    count_fail = 0
    count_skip = 0

    res = dict(zip(test_cases, statuses))
    for test_case, status in res.items():
        print(f"{test_case} — {status}")

        if status == "PASS":
            count_pass += 1
        elif status == "FAIL":
            count_fail += 1
        elif status == "SKIP":
            count_skip += 1

    print(f"Успешных: {count_pass}")
    print(f"Неуспешных: {count_fail}")
    print(f"Пропущено: {count_skip}")

    if count_fail > 0:
        print("Запуск не успешный")

result = print_report(test_cases, statuses)