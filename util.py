import datetime


# getting starting time and return it
from heapq import merge


def start_watch():
    start = datetime.datetime.now().microsecond
    return start


# getting Elapsed time
def stop_watch(start):
    stop = datetime.datetime.now().microsecond
    return stop - start


# Bubble sort for integer
def BubbleSort(arr):
    N = len(arr)
    for i in range(N):
        for j in range(0, N - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print(arr[i])


#  Bubble sort for string

def BubbleSortString(str):
    N = len(str)
    for i in range(N - 1):
        for j in range(i + 1, N):
            if str[j] <= str[i]:
                str[j], str[i] = str[i], str[j]
    return str


# Insertion sort for Integer Number

def InsertionSortNum(arr):
    N = len(arr)
    for i in range(1, N):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# Insertion sort for String element

def InsertionSortString(str1):
    N = len(str1)
    for i in range(1, N):
        key = str1[i]
        j = i - 1
        while j >= 0 and str1[j] > key:
            str1[j + 1] = str1[j]
            j -= 1
        str1[j + 1] = key


# Binary Search for Integer Element

def BinarySearchNumber(arr, start, last, key):
    while start <= last:
        mid = int((start + last) / 2)
        if arr[mid] == key:
            return 1
        elif arr[mid] < key:
            start = mid + 1
        elif arr[mid] > key:
            last = mid - 1
    return -1


# Binary search for string element

def BinarySearchString(str1, key):
    first = 0
    last = len(str1) - 1

    while first <= last:
        mid = int((first + last) / 2)
        if str1[mid] == key:
            return 1
        elif str1[mid] < key:
            first = mid + 1
        elif str1[mid] > key:
            last = mid - 1
    return -1




# Merge Sort

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
# Find the middle point and devide it
    middle = len(arr) // 2
    left_list = arr[:middle]
    right_list = arr[middle:]

    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)
    return list(merge(left_list, right_list))

# Merge the sorted halves

def merge(left_half,right_half):

    res = []
    while len(left_half) != 0 and len(right_half) != 0:
        if left_half[0] < right_half[0]:
            res.append(left_half[0])
            left_half.remove(left_half[0])
        else:
            res.append(right_half[0])
            right_half.remove(right_half[0])
    if len(left_half) == 0:
        res = res + right_half
    else:
        res = res + left_half
    return res