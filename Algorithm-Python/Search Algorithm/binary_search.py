# coding:utf-8
# Author: Neacik
from builtins import len


# Test

def binary_search_recurse(arr, k, low, high):
    if low <= high:
        mid = (low + high) / 2
        if arr[mid] == k:
            return mid
        elif arr[mid] < k:
            return binary_search_recurse(arr, k, mid + 1, high)
        else:
            return binary_search_recurse(arr, k, low, mid - 1)
    else:
        return -1  # 没找到时返回-1


def binary_search_unrecurse(arr, k):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) / 2
        if arr[mid] == k:
            return mid
        elif arr[mid] < k:
            low = mid + 1
        else:
            high = mid - 1
    return -1
