from week1.Algorithm.utility.util import InsertionSortString


def main():
    str = ["Pune", "Nagpur", "Delhi", "Chennai", "Mumbai"]
    InsertionSortString(str)
    print("Sorted string:")
    for i in range(len(str)):
        print(str[i])


if __name__ == "__main__":
    main()
