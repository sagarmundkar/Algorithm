# import util_class

from week1.Algorithm.utility.util_class import anagram


def main():
    str1 = input("Enter the first string:")
    str2 = input("Enter the second string:")
    if anagram(str1, str2):
        print("String are anagram.")
    else:
        print("String are not anagram.")


# driver code.

if __name__ == '__main__':
    main()
