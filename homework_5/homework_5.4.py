result_test = input("Введите результат теста: ").upper().strip()


class InvalidTestStatusError(Exception):
    pass


try:
    if result_test not in ['PASS', 'FAIL', 'SKIP']:
        raise InvalidTestStatusError(
            f'Неизвестный статус теста {result_test}'
        )
    print(f'Статус: {result_test}')
except InvalidTestStatusError as e:
    print(f"Ошибка тестовых данных: {e}")
