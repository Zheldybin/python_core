from functools import reduce

test_results = [
    {'name': 'test_login', 'status': 'PASS', 'time': 2.5},
    {'name': 'test_registration', 'status': 'FAIL', 'time': 3.1},
    {'name': 'test_profile', 'status': 'PASS', 'time': 1.8},
    {'name': 'test_payment', 'status': 'FAIL', 'time': 4.2},
    {'name': 'test_api', 'status': 'SKIP', 'time': 0.5},
    {'name': 'test_security', 'status': 'PASS', 'time': 5.0},
    {'name': 'test_performance', 'status': 'SKIP', 'time': 10.0}
]

failed_tests = list(filter(lambda test: test['status'] == 'FAIL', test_results))
failed_test_names = list(map(lambda test: test['name'], failed_tests))
name_tests = list(map(lambda x: x['name'], test_results))
full_time_tests = reduce(lambda x, y: x + y, map(lambda x: x['time'], test_results))
successful_tests_name = [test['name'] for test in test_results if test['status'] == 'PASS']

pass_tests = 0
skip_tests = 0
fail_tests = 0

for test in test_results:
    if test["status"] == "PASS":
        pass_tests += 1
    elif test["status"] == "FAIL":
        fail_tests += 1
    else:
        skip_tests += 1

print(f'Успешных тестов было - {pass_tests}')
print(f'Пропущеных тестов было - {skip_tests}')
print(f'Упавших тестов было - {fail_tests}')
print(f'Список успешных тестов {successful_tests_name}')
print(f'Список упавших тестов {failed_test_names}')
print(f'Общее время выполнения всех тестов составило: {full_time_tests} секунд')