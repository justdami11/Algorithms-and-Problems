#This program implements the binary search algorithm to find the position of a target number in a sorted list.
#It returns the index of the target if found, or -1 if the target is not in the list.


def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def main():
    data = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37,
            41, 45, 49, 53, 57, 61, 65, 69, 73, 77,
            81, 85, 89, 93, 97, 101, 105, 109, 113, 117,
            121, 125, 129, 133, 137, 141, 145, 149, 153, 157,
            161, 165, 169, 173, 177, 181, 185, 189, 193, 197]

    target = 85
    index = binary_search(data, target)

    if index != -1:
        print(f"Value {target} found at index {index}.")
    else:
        print(f"Value {target} not found in the list.")


if __name__ == "__main__":
    main()
