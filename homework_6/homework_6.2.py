def create_time_checker(max_time):
    def inner(time_test):
        if time_test > max_time:
            print(f"Превышен лимит {max_time} секунд на {time_test - max_time}")
        else:
            print(f"Лимит {max_time} не превышен")
    return inner

result_5 = create_time_checker(5)
result_10 = create_time_checker(10)

result_5(3)
result_5(8)