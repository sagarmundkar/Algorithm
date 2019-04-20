from week1.Algorithm.utility.util import BinarySearchNumber


def main():
    arr = [10, 23, 31, 13, 42, 7]
    print(arr)
    start = 0
    last = len(arr) - 1
    key = int(input("Enter the key value:"))
    arr = sorted(arr)
    result = BinarySearchNumber(arr, start, last, key)
    print(result)
    if result == -1:
        print("Element not present")
    else:
        print("Element found")


if __name__ == "__main__":
    main()
