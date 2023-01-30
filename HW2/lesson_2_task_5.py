m = int(input("Введите номер месяца: "))

def month_to_season(m):
    if m in range(3, 6):
        return("Весна")
    elif m in range(6, 9):
        return("Лето")
    elif m in range(9, 12):
        return("Осень")
    elif m == 1 or m == 2 or m == 12:
        return("Зима")

s = month_to_season(m)

print("Сезон:", s)