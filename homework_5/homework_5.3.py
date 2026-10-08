def tests(running_tests, timeout):
    # Создаём ошибки на некорректные тесты
    if running_tests < 0 or running_tests > 5:
        raise ValueError("Количество повторных запусков должно быть от 0 до 5")
    if timeout < 0:
        raise ValueError("Таймаут должен быть положительным числом")

result_tests = [
    {"running_tests": 3, "timeout": 3},
    {"running_tests": 4, "timeout": -1},
    {"running_tests": 6, "timeout": 3.5}
]

for test in result_tests:
    try:
        running_tests = test["running_tests"]
        timeout = test["timeout"]
        tests(running_tests, timeout)

    except ValueError as e:
        print(e)
    else:
        print("Тест прошел успешно!")