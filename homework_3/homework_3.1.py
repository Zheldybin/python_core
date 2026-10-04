result_tests = input("Введите результаты теста через пробел: ").upper().split()
count_all_tests = len(result_tests)

def get_test_statistics(arr):
    stats = {"PASS": 0, "FAIL": 0, "SKIP": 0}
    for n in arr:
        if n == "PASS":
            stats["PASS"] += 1
        elif n == "FAIL":
            stats["FAIL"] += 1
        elif n == "SKIP":
            stats["SKIP"] += 1
    return stats

stats = get_test_statistics(result_tests)

success_rate = stats['PASS'] / count_all_tests * 100

print(f"Всего тестов: {count_all_tests}")
print(f"PASS: {stats['PASS']}")
print(f"SKIP: {stats['SKIP']}")
print(f"FAIL: {stats['FAIL']}")
print(f"Успешно: {success_rate}")