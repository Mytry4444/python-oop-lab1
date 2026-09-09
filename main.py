import math
from root import root

try:
    x = float(input("give your value for x: "))

    if x < 0:
        print("Помилка: Неможливо обчислити квадратний корінь з від'ємного числа!")
    else:
        print("System sqrt:", math.sqrt(x))
        print("Custom root:", root(x))

except ValueError:
    print("Помилка: Ви ввели не число! Будь ласка, введіть числове значення.")