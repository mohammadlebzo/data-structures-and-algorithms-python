
def insertion_sort(array):

    for i in range(1, len(array)):
        j = i - 1
        temp = array[i]

        while j >= 0 and temp < array[j]:
            array[j + 1] = array[j]
            j = j - 1

        array[j + 1] = temp


if __name__ == "__main__":
    arr = [8, 4, 23, 42, 16, 15]
    arr2 = [20, 18, 12, 8, 5, -2]
    arr3 = [5, 12, 7, 5, 5, 7]
    arr4 = [2, 3, 5, 7, 13, 11]
    insertion_sort(arr)
    insertion_sort(arr2)
    insertion_sort(arr3)
    insertion_sort(arr4)
    print(arr)
    print(arr2)
    print(arr3)
    print(arr4)

