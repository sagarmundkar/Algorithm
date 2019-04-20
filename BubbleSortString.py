from week1.Algorithm.utility.util import BubbleSortString


def main():
    str = ["Pune", "Nagpur", "Delhi", "Chennai", "Mumbai"]
    BubbleSortString(str)
    print("Sorted string:")
    for i in range(len(str)):
        print(str[i])


if __name__ == "__main__":
    main()