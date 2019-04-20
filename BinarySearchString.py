from week1.Algorithm.utility.util import BinarySearchString


def main():
    str1 = ["Pune", "Nagpur", "Delhi", "Chennai", "Mumbai"]
    key = input("Enter the key:")
    str1 = sorted(str1)

    result = BinarySearchString(str1, key)
    if result == -1:
        print("Element not present")
    else:
        print("Element found")


if __name__ == "__main__":
    main()
