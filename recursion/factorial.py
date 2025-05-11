#This program calculates the factorial of a non-negative integer using recursion.
#The user is prompted to enter a number, and the program will display the factorial result.
#It exits when the user types 'q'.


def factorial(n):

    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0:
        return 1
    return n * factorial(n - 1)


def main():
    print("\n<<< Factorial Calculator — Enter a non-negative integer (or 'q' to quit) >>>\n")
    while True:
        user_input = input("Enter n: ")

        if user_input.lower() == 'q':
            print("Exiting program.")
            break

        try:
            n = int(user_input)
            result = factorial(n)
            print(f"{n}! = {result}")
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()

