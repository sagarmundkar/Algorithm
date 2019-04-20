from week1.Algorithm.utility.util_class import DayOfWeek


def main():
    d = int(input("Enter the day:"))
    m = int(input("Enter the month:"))
    y = int(input("Enter the year:"))

    print(DayOfWeek(d, m, y))


if __name__ == '__main__':
    main()
