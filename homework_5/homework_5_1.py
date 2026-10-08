from functools import reduce
import json

def open_file(file):
    with open(file, 'r', encoding='utf-8') as f:
        test_results = json.load(f)
    return test_results

def failed_test_names(test_results):
    failed_tests = list(filter(lambda test: test['status'] == 'FAIL', test_results))
    failed_test_names = list(map(lambda test: test['name'], failed_tests))
    return failed_test_names
    
def full_time_tests(test_results):
    refull_time_tests = reduce(lambda x, y: x + y, map(lambda x: x['time'], test_results))
    return refull_time_tests

def successful_tests(test_results):
    successful_tests_name = [test['name'] for test in test_results if test['status'] == 'PASS']
    return successful_tests_name

def count_status(test_results):
    counts = {"PASS": 0, "FAIL": 0, "SKIP": 0}
    for test in test_results:
        if test['status'] == "PASS":
            counts['PASS'] += 1
        elif test["status"] == "FAIL":
            counts['FAIL'] += 1
        elif test["status"] == "SKIP":
            counts['SKIP'] += 1
    return counts

test_results = open_file('result_test.json')
counts = count_status(test_results)

print(f"Успешных тестов было - {counts['PASS']}")
print(f"Пропущенных тестов было - {counts['SKIP']}")
print(f"Упавших тестов было - {counts['FAIL']}")
print(f"Список успешных тестов {successful_tests(test_results)}")
print(f"Список упавших тестов {failed_test_names(test_results)}")
print(f"Общее время выполнения всех тестов составило: {full_time_tests(test_results)} секунд")