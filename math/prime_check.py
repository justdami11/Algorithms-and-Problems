# This program checks whether a given number is a prime number.
# A prime number is a positive integer greater than 1 that has no divisors other than 1 and itself.

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def main():
    print("\n<<< Prime Number Checker >>>\n")

    while True:
        user_input = input("Enter a number to check ('q' to quit): ").strip()

        if user_input.lower() == 'q':
            print("Exiting program.")
            break

        try:
            number = int(user_input)
            if is_prime(number):
                print(f"The number {number} is a prime number.\n")
            else:
                print(f"The number {number} is NOT a prime number.\n")
        except ValueError:
            print("Invalid input. Please enter a valid integer.\n")


if __name__ == "__main__":
    main()
