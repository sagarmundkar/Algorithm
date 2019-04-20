import math

# String Anagram

import numpy as np


def anagram(str1, str2):
    if sorted(str1) == sorted(str2):
        return True
    else:
        return False


############################################################################################

# prime number

def PrimeNumber(rng):
    for Num1 in range(1, 1000):
        count = 0
        for j in range(2, (Num1 // 2 + 1)):
            if Num1 % j == 0:
                count = count + 1
                break
        if count == 0 and Num1 != 1:
            print("%d" % Num1)


##################################################################################################
def is_anagram(str1, str2):
    if len(str1) == len(str2):
        arr = np.full((len(str2)), False)
        cnt = 0
        for i in range(len(str1)):
            for j in range(len(str2)):
                if str1[i] == str2[j] and arr[j] == False:
                    arr[j] = True
                    cnt += 1
                    break
    else:
        return False
    if cnt == len(str1):
        return True


#################################################################################################################

def isPrime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def get_prime_number(rng):
    arr = []
    for i in range(2, rng + 1):
        if isPrime(i):
            arr.append(i)
    return arr


########################################################################################################################


def is_palindrome(n):
    new = n
    reverse = 0
    while new != 0:
        temp = int(new % 10)
        new = int(new / 10)
        reverse = (reverse * 10) + temp
        if n == reverse:
            return True
        else:
            return False


def get_palindrome(arr):
    newArr = []
    for i in arr:
        if is_palindrome(i):
            newArr.append(i)
    return newArr


########################################################################################################################

def is_anagram(str1, str2):
    if len(str1) == len(str2):
        arr = np.full((len(str2)), False)
        cnt = 0
        for i in range(len(str1)):
            for j in range(len(str2)):
                if str1[i] == str2[j] and arr[j] == False:
                    arr[j] = True
                    cnt += 1
                    break
    else:
        return False
    if cnt == len(str1):
        return True


def get_anagram(arr):
    newArr = []
    for i in range(len(arr) - 1):
        for j in range(1 + i, len(arr)):
            if is_anagram(str(arr[i]), str(arr[j])):
                newArr.append(arr[i])
                newArr.append(arr[j])
    return newArr


##################################################################################################################

# get days:

def week(i):
    switcher = {
        0: "Sunday",
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday"
    }
    return switcher.get(i)


########################################################################################################################


# DayOfWeek

def DayOfWeek(d, m, y):
    y0 = y - (14 - m) / 12
    x = y0 + y0 / 4 - y0 / 100 + y0 / 400
    m0 = m + 12 * ((14 - m) / 12) - 2
    d0 = (d + x + 31 * m0 / 12) % 7
    return week(int(d0))


########################################################################################################################

# calculating Celsius To Fahrenheit temperature

def CelsiusToFahrenheit(temp):
    ftemp = (temp * 9 / 5) + 32
    return ftemp


########################################################################################################################

# calculating  Fahrenheit To Celsius temperature

def FahrenheitToCelsius(temp):
    ctemp = (temp - 32) * 5 / 9
    return ctemp


########################################################################################################################

# Calculating monthly payment

def Payment(P, Y, R):
    n = 12 * Y
    r = R / (12 * 100)
    payment = (P * r) / 1 - (1 + r) * math.pow((1 + r), (-n))
    return payment


########################################################################################################################

# Square root of non-negative number

def SqrtNumber(c):
    t = c
    epsilon = 1 * math.e - 15
    while abs(t - c / t) > epsilon * t:
        t = (c / t + t) / 2
        return abs(t)
    print("Square root of c is:", t)


########################################################################################################################

# Calculating minimum number of notes as Vending machine

def VendingMachine(change):
    arr = (1000, 500, 100, 50, 10, 5, 2, 1)
    for i in arr:
        if change == 0:
            return 0
        elif change >= i:
            print(i)
            change = VendingMachine(change - i)


########################################################################################################################
# Bubble Sort

def BubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return arr


########################################################################################################################

# Binary Search

def BinarySearch(arr, start, last, key):
    while start <= last:
        mid = int((start + last) / 2)
        if arr[mid] == key:
            return 1
        elif arr[mid] < key:
            start = mid + 1
        elif arr[mid] > key:
            last = mid - 1
        return -1


########################################################################################################################


# read data from file and stored in list

def read_from_file():
    f = open("abc.txt", 'r').readline()
    # print(f.read())
    word = " "
    for i in f:
        word = word + i
        st = word.split("\n")
        sts = BubbleSort(list(st))
    return sts


########################################################################################################################

# search key in sorted list

def word_list(key, sts):
    print(sts)
    mid = BinarySearch(sts, 0, len(sts) - 1, key)
    if mid is None:
        return False
    return True


# Decimal Convert into Binary

def to_binary(n):
    tm = np.zeros(8)
    res = np.zeros(8)
    i = 0
    while n != 0:
        temp = int(n % 2)
        n = int(n / 2)
        tm[i] = temp
        i += 1
    i = 8
    for j in tm:
        i -= 1
        res[i] = j
    return res


# Binary Number convert into Decimal

def to_decimal(binary):
    j = 7
    res = 0
    for i in binary:
        if i == 1:
            res = res + math.pow(2, j)
        j -= 1
    return int(res)


# swap number

def swap_nibbles(binary):
    j = 4
    for i in range(4):
        binary[i], binary[j] = binary[j], binary[i]
        j += 1
    return binary


# Question Number

def question_to_find_your_number(start, last):
    while start <= last:
        mid = int((start + last) / 2)
        if input("are you guess this number : ", mid) == 1:
            print("Number found.")
            break
        elif int(input("If your number will greater than then enter 1 else 0 : ", mid)) == 1:
            start = mid + 1
            continue
        elif int(input("If your number will less than then enter 1 else 0 : ", mid)) == 1:
            last = mid - 1
