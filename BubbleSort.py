# Bubble Sort For integer
from week1.Algorithm.utility.util import BubbleSort, start_watch, stop_watch, BubbleSortString


def main():
    arr = [23, 4, 52, 13, 32, 16, 7]
    str = ["Pune", "Nagpur", "Delhi", "Chennai", "Mumbai"]

# Sorting numbers

    print("Bubble Sorted array:")
    BubbleSort(arr)
    for i in range(len(arr)):
        print(arr[i])
    start = start_watch()
    print("Elapse time : ", stop_watch(start))

# String Sorting

    print("Bubble Sorted String:")
    BubbleSortString(str)
    for i in range(len(str)):
        print(str[i])
    start = start_watch()
    print("Elapse time : ", stop_watch(start))


if __name__ == "__main__":
    main()
