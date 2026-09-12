import math

number_1 = -1.6
number_2 = 2.99

# преобразование из float в int дробная часть отбрасывается
result_1 = int(number_1)
result_2 = int(number_2)
# округление к ближайшему числу
result_3 = round(number_1)
result_4 = round(number_2)
# округление в большую сторону
result_5 = math.ceil(number_1)
# округление в меньшую сторону
result_6 = math.floor(number_2)

print(result_1)
print(result_2)
print(result_3)
print(result_4)
print(result_5)
print(result_6)