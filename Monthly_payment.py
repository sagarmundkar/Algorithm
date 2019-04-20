# Calculating the monthly payment using the formula

from week1.Algorithm.utility.util_class import Payment


def main():
    P = int(input("Enter the payment:"))
    Y = int(input("Enter the year:"))
    R = int(input("Enter the rate:"))
    print(Payment(P, Y, R))


if __name__ == "__main__":
    main()