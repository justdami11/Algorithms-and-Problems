#This program checks whether a given word is a palindrome.
#A palindrome is a word that reads the same backward as forward.

def is_palindrome(word):
    return word == word[::-1]


def main():
    print("\n<<< Palindrome Checker>>>\n")

    while True:
        word = input("Enter a word to check ('q' to quit): ").strip()

        if word.lower() == 'q':
            print("Exiting program.")
            break

        if is_palindrome(word):
            print(f"The word '{word}' is a palindrome.\n")
        else:
            print(f"The word '{word}' is not a palindrome.\n")


if __name__ == "__main__":
    main()
