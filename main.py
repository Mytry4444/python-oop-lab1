import math
from root import root

print("=== Програма порівняння системного та власного квадратного кореня ===")

try:
    x = float(input("Введіть невід'ємне число для обчислення кореня (наприклад, 16): "))

    if x < 0:
        print("\nПомилка: Неможливо обчислити квадратний корінь з від'ємного числа!")
    else:
        system_result = math.sqrt(x)
        custom_result = root(x)
        
        print("\n--- Результати обчислень ---")
        print(f"1. Результат системної функції (math.sqrt): {system_result}")
        print(f"2. Результат власної функції з модуля root:  {custom_result}")

except ValueError:
    print("\nПомилка: Ви ввели не число! Будь ласка, введіть числове значення.")