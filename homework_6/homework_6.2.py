def create_time_checker(max_time):
    def inner(time_test):
        if time_test > max_time:
            print(f"Превышен лимит {max_time} секунд на {time_test - max_time}")
        else:
            print(f"Лимит {max_time} не превышен")
    return inner

result = create_time_checker(5)
print(result(10))