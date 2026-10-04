with open('number.txt', 'r') as f_in, \
     open('even_numbers.txt', 'w') as f_even, \
     open('odd_numbers.txt', 'w') as f_odd:

    for line in f_in:
        line = line.strip()
        number = int(line)
        if number % 2 == 0:
            f_even.write(f"{number}\n")
        else:
            f_odd.write(f"{number}\n")
