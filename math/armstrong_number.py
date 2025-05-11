# This program checks whether a given number is an Armstrong number.
# An Armstrong number is a number that is equal to the sum of its own digits
# each raised to the power of the number of digits.

def is_armstrong_number(n):
    total = 0
    lenght = len(str(n))
    for i in str(n):
        total += (int(i) ** lenght)
    return total == n 


def main():
    print("\n<<< Armstrong Number Checker >>>\n")

    while True:
        user_input = input("Enter a number to check (or 'q' to quit): ").strip()

        if user_input.lower() == 'q':
            print("Exiting program.")
            break

        try:
            number = int(user_input)
            if is_armstrong_number(number):
                print(f"The number {number} is an Armstrong number.\n")
            else:
                print(f"The number {number} is NOT an Armstrong number.\n")
        except ValueError:
            print("Invalid input. Please enter a valid integer.\n")


if __name__ == "__main__":
    main()
