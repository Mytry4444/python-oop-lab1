import math
from root import root

print("=== Програма порівняння системного та власного квадратного кореня ===")

while True:
    user_input = input("\nВведіть невід'ємне число (або 'exit' для виходу): ").strip()

    if user_input.lower() == 'exit':
        print("Завершення роботи програми. До побачення!")
        break

    try:
        x = float(user_input)

        if x < 0:
            print("Помилка: Неможливо обчислити квадратний корінь з від'ємного числа!")
        else:
            system_result = math.sqrt(x)
            custom_result = root(x)
            
            print("--- Результати обчислень ---")
            print(f"1. Результат системної функції (math.sqrt): {system_result}")
            print(f"2. Результат власної функції з модуля root:  {custom_result}")

    except ValueError:
        print("Помилка: Ви ввели не число! Будь ласка, введіть числове значення.")