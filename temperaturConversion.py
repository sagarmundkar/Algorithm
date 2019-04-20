from week1.Algorithm.utility.util_class import CelsiusToFahrenheit, FahrenheitToCelsius


def main():
    temp = int(input("Enter the temperature:"))
    print(CelsiusToFahrenheit(temp))
    print(FahrenheitToCelsius(temp))


if __name__ == '__main__':
    main()
