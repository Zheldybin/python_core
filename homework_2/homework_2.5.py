all_tests = int(input("Введите количество выполненных тестов: "))
result_tests = []
count_pass = 0
count_fail = 0
count_skip = 0

if all_tests <= 0:
    print("количество тестов должно быть больше или равно 0")
else:
    for i in range(0, all_tests):
        result_test = input("Введите по очереди результаты тестов: ").upper()
        if result_test == "PASS" or result_test == "FAIL" or result_test == "SKIP":
            result_tests.append(result_test)
        else:
            continue

for i in range(0, len(result_tests)):
    if result_tests[i] == "PASS":
        count_pass += 1
    elif result_tests[i] == "FAIL":
        count_fail += 1
    elif result_tests[i] == "SKIP":
        count_skip += 1

if count_fail > 0:
    print(f"Тесты не прошли. Количество не успешных тестов {count_fail}")
else:
    print(f"Тестирование прошло. Успеншых тестов {count_pass}, пропущеных тестов {count_skip}")

