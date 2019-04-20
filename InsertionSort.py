from week1.Algorithm.utility.util import InsertionSortNum, start_watch, stop_watch, InsertionSortString


def main():
    arr = [12, 3, 23, 41, 8, 15]
    str1 = ["Pune", "Nagpur", "Delhi", "Chennai", "Mumbai"]

    InsertionSortNum(arr)
    print("Insertion Sorted array:")
    for i in range(len(arr)):
        print(arr[i])
    start = start_watch()
    print("Elapse time : ", stop_watch(start))

    InsertionSortString(str1)
    print("Insertion Sorted string:")
    for i in range(len(str1)):
        print(str1[i])
    start = start_watch()
    print("Elapse time : ", stop_watch(start))


if __name__ == "__main__":
    main()
