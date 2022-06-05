def binary_search(arr, num):
    """
    This function preforms a Binary Search to search for
    a specific given number.
    :param arr: The list of numbers
    :param num: The number to search for
    :return: number
    """
    length = len(arr) -1
    start = 0
    while start <= length:
        mid_point = start + (length - start) // 2

        if arr[mid_point] == num:
            return mid_point
        elif arr[mid_point] < num:
            start = mid_point + 1
        else:
            length = mid_point - 1

    return -1

print(binary_search([4, 8, 15, 16, 23, 42], 15))
print(binary_search([-131, -82, 0, 27, 42, 68, 179], 42))
print(binary_search([11, 22, 33, 44, 55, 66, 77], 90))
print(binary_search([1, 2, 3, 5, 6, 7], 4))