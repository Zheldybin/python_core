from functools import wraps


def log_test(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Запуск теста: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Функция выполнена результат {result}")
        return result

    return wrapper


@log_test
def sum(a, b):
    print("Выполняется функция")
    result = a + b
    return result


sum(2, 3)
