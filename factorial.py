def factorial(number):
    if number < 0:
        print("Factorial is not defined for negative numbers.")

    elif number == 0 or number == 1:
        return 1
    else:
        result = 1
        for i in range(2, number + 1):
            result *= i
        return result