#This program performs a linear search to find a target number in an unsorted list.
#It returns the index of the target if found, or None if not found.

def bubble_sort(data):
    n = len(data)
    for x in range(n -1):
        for i in range(n -1 - x):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
    return data

def main():
    data = [83, 12, 67, 91, 55, 9, 28, 76, 3, 42,
            87, 35, 64, 21, 18, 50, 79, 33, 90, 27,
            5, 62, 46, 38, 25, 73, 1, 97, 30, 14,
            84, 69, 17, 22, 99, 81, 58, 60, 44, 6,
            19, 15, 11, 100, 8, 36, 2, 16, 59, 24]

    print(bubble_sort(data))



if __name__ == "__main__":
    main()
