#This program checks whether two input words are anagrams of each other.
#It compares the frequency of letters in both words using dictionaries.
#The program continues running until the user types 'q' to quit.


def anagram_checker(word_1, word_2):
    if len(word_1) != len(word_2):
        return False

    letter_count_1 = {}
    letter_count_2 = {}

    for letter in word_1:
        letter_count_1[letter] = letter_count_1.get(letter, 0) + 1

    for letter in word_2:
        letter_count_2[letter] = letter_count_2.get(letter, 0) + 1


    return letter_count_1 == letter_count_2


def main():
    print("\n<<< Anagram Checker >>>\n")

    while True:
        word_1 = input("Enter the first word ('q' to quit): ").strip()
        if word_1.lower() == 'q':
            print("Exiting program.")
            break

        word_2 = input("Enter the second word: ").strip()

        if anagram_checker(word_1.lower(), word_2.lower()):
            print("Yes, they are anagrams!\n")
        else:
            print("No, they are not anagrams.\n")


if __name__ == "__main__":
    main()
