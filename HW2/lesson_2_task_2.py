y = int(input())

def is_year_leap(x):
    if x % 4 == 0:
        return True
    else:
        return False

is_year_leap(y)

b = is_year_leap(y)

print("год", y, ":", b)

