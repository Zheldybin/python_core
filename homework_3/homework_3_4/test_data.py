import random

logins = ["admin", "user_1", "user_2", "user_3", "user_4", "user_5", "user_6", "user_7", "user_8", "user_9"]
statuses = ["ACTIVE", "BLOCKED", "INACTIVE"]


def generate_login():
    return random.choice(logins)


def generate_age():
    return random.randint(1, 100)


def generate_status():
    return random.choice(statuses)


def generate_user():
    return {
        "login": generate_login(),
        "age": generate_age(),
        "status": generate_status(),
    }
