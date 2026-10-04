with open('number.txt', 'r') as f:
    file = f.readlines()
    if len(file) < 3:
        print("В файле чисел меньше 3х")
    else:
        print(file[0].strip())
        print(file[1].strip())
        print(file[len(file) - 2].strip())
        print(file[len(file) - 1].strip())
