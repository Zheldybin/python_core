import json
try:
    with open('account.json', 'r', encoding='utf-8') as f:
        account = json.load(f)

        for user in account:
            if 'login' not in user:
                raise KeyError('login')
            if 'password' not in user:
                raise KeyError('password')
            if 'result' not in user:
                raise KeyError('result')
            print(user)

except FileNotFoundError as e:
    print(f'Файл не найден: {e}')
except json.JSONDecodeError as e:
    print(f'Содержание файла не является JSON: {e}')
except KeyError as e:
    print(f'У пользователя отсутсвует обязательное поле {e}')