def factorial(n):
#Recursively calculates the factorial of a non-negative integer n.
    
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0:
        return 1
    return n * factorial(n - 1)


def main():
    
    #Prompts the user to enter numbers and calculates their factorials.
    #The program exits when the user enters 'q'.
    
    print("Factorial Calculator — Enter a non-negative integer (or 'q' to quit)")
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
