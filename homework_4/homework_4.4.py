with open('bin_1.bin', 'rb') as f:
    data_1 = f.read()

with open('bin_2.bin', 'rb') as f:
    data_2 = f.read()

with open('bin_2.bin', 'wb') as f:
    f.write(data_1)

with open('bin_1.bin', 'wb') as f:
    f.write(data_2)