def merge_sort(arr):
    n = len(arr)

    if n > 1:

        mid = n//2

        left = arr[:mid]
        right = arr[mid:]

        # Sorting the first half
        merge_sort(left)

        # Sorting the second half
        merge_sort(right)

        merge(left, right, arr)


def merge(left, right, arr):
    i = j = k = 0

    # Copy data to temp arrays L[] and R[]
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # Checking if any element was left
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


if __name__ == "__main__":
    arr1 = [8, 4, 23, 42, 16, 15]
    arr2 = [20, 18, 12, 8, 5, -2]
    arr3 = [5, 12, 7, 5, 5, 7]
    arr4 = [2, 3, 5, 7, 13, 11]
    merge_sort(arr1)
    merge_sort(arr2)
    merge_sort(arr3)
    merge_sort(arr4)
    print(arr1)
    print(arr2)
    print(arr3)
    print(arr4)

