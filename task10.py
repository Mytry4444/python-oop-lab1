try:
    years = int(input("Введіть ваш вік у роках: "))
    
    if years < 0 or years > 120:
        print("Помилка: Некоректний вік!")
    else:
        days = years * 365
        print(f"Ваш вік: {years} років або {days} днів.")

except ValueError:
    print("Помилка: Введіть вік цілим числом!")