print("=== Програма конвертації віку з років у дні ===")

while True:
    try:
        user_input = input("\nВведіть ваш вік у роках (або '0' для виходу): ").strip()
        
        # Перевірка на вихід з програми
        if user_input == '0' or user_input.lower() == 'exit':
            print("Завершення роботи програми. До побачення!")
            break

        years = int(user_input)

        if years < 0 or years > 120:
            print("Помилка: Введіть реальний вік у діапазоні від 1 до 120 років!")
        else:
            days = years * 365
            print(f"Результат: Ваш вік {years} років (це приблизно {days} днів).")

    except ValueError:
        print("Помилка: Введіть вік цілим числом, а не текстом чи дробом!")