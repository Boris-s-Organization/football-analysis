
def binary_search(arr, x):
    """
    Searches for the element x in the sorted array arr using binary search.
    Returns the index of the element if found, else returns -1.
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1

print(binary_search([1, 2, 3, 4, 5], 3)) # 2