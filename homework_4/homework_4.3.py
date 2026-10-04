with open('number.txt', 'r') as f:
    lines = f.readlines()

with open('number.txt', 'w') as f:
    for line in lines:
        line = line.strip()
        number = float(line)
        squared = number ** 2
        f.write(f'{squared}\n')