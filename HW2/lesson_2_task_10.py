x = int(input("Размер вклада: "))
y = int(input("Срок вклада:"))

def bank(x, y):
    for n in range(1, y + 1):
        x = x + x * 0.1
    return x

s = bank(x, y)
    
print("Сумма, которая будет на счету пользователя, спустя", y, "лет:", s)