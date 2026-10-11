from functools import wraps


def retry(count):
    def inner(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            for x in range(count):
                print(f"Попытка: {x + 1}")
                result = func(*args, **kwargs)
                if result == True:
                    print("Запуск закончен")
                    break
            return result

        return wrapper

    return inner


count_test = [0]


@retry(5)
def test():
    if count_test[0] == 2:
        return True
    else:
        count_test[0] += 1
        return False


test()
