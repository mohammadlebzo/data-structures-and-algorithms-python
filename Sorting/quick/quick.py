def quick_sort(arr, left, right):
    if left < right:
        position = partition(arr, left, right)

        quick_sort(arr, left, position - 1)

        quick_sort(arr, position + 1, right)


def partition(arr, left, right):
    pivot = arr[right]
    low = left - 1

    for i in range(left, right):
        if arr[i] <= pivot:
            low += 1
            swap(arr, i, low)

    swap(arr, right, low + 1)

    return low + 1


def swap(arr, i, low):
    temp = arr[i]
    arr[i] = arr[low]
    arr[low] = temp


if __name__ == "__main__":
    arr1 = [8, 4, 23, 42, 16, 15]
    arr2 = [20, 18, 12, 8, 5, -2]
    arr3 = [5, 12, 7, 5, 5, 7]
    arr4 = [2, 3, 5, 7, 13, 11]
    quick_sort(arr1, 0, len(arr1) - 1)
    quick_sort(arr2, 0, len(arr1) - 1)
    quick_sort(arr3, 0, len(arr1) - 1)
    quick_sort(arr4, 0, len(arr1) - 1)
    print(arr1)
    print(arr2)
    print(arr3)
    print(arr4)

