FIRST_POSITIVE_INTEGER = 1


def factorial(number):
    product = FIRST_POSITIVE_INTEGER
    for factor in range(FIRST_POSITIVE_INTEGER, number + 1):
        product *= factor
    return product


if __name__ == "__main__":
    number = 5
    print(f"Factorial of {number} is {factorial(number)}")
