import sys
import homework_5.homework_5_1 as hw_one
import json


def all_test_count(count_status):
    all_tests = count_status["PASS"] + count_status["FAIL"] + count_status["SKIP"]
    print(f"Всего выполненно тестов: {all_tests}")
    return all_tests


def longest_duration_test(test_results):
    longest_duration = max(t['time'] for t in test_results)
    print(f"Самый длинный тест: {longest_duration} секунд")
    return longest_duration


def validation(test_results):
    for test in test_results:
        if 'name' not in test:
            raise KeyError('name')
        if 'status' not in test:
            raise KeyError('status')
        if 'time' not in test:
            raise KeyError('time')


try:
    test_results = hw_one.open_file('result_test.json')
    validation(test_results)
    counts = hw_one.count_status(test_results)
except FileNotFoundError as e:
    print(f'Файл не найден: {e}')
    sys.exit(1)
except json.JSONDecodeError as e:
    print(f'Содержание файла не является JSON: {e}')
    sys.exit(1)
except KeyError as e:
    print(f"Некорректная структура данных: {e}")
    sys.exit(1)

report = {
    "total": all_test_count(counts),
    "pass": counts["PASS"],
    "fail": counts["FAIL"],
    "skip": counts["SKIP"],
    "failed_tests": hw_one.failed_test_names(test_results),
    "successful_tests": hw_one.successful_tests(test_results),
    "longest_duration": longest_duration_test(test_results),
    "total_time": hw_one.full_time_tests(test_results),
}

with open('report.json', 'w', encoding='utf-8') as f:
    json.dump(report, f, indent=4)
print("Отчёт сохранён в report.json")
