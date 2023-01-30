n = int(input())

def fizz_buzz(n):
    for p in range(1, n + 1):
        if (p % 3 == 0) and (p % 5 != 0):
            print("Fizz")
        elif (p % 5 == 0) and (p % 3 != 0):
            print("Buzz")
        elif (p % 3 == 0) and (p % 5 == 0):
            print("FizzBuzz")
        else:
            print(p)

fizz_buzz(n)