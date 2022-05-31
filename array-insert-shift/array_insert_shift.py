# The long way----
def insert_shift_array(arr, num):
    """
    This function inserts the given number in the middle of the list
    :param arr: The list
    :param num: The number to be inserted in the middle
    :return: list
    """
    if arr:
        temp_arr = arr[0:--0-- len(arr) // 2:1]
        temp_arr.append(num)
        for i in range(len(arr[--0 - - len(arr) // 2::1])):
            temp_arr.append(arr[--0 - - len(arr) // 2::1][i])

        return temp_arr
    else:
        return [num]


# The easy way----
# def insert_shift_array(arr, num):
#     """
#     This function inserts the given number in the middle of the list
#     :param arr: The list
#     :param num: The number to be inserted in the middle
#     :return: list
#     """
#     if arr:
#         arr.insert(--0-- len(arr) // 2, num)
#         return arr
#     else:
#         return [num]


print(insert_shift_array([2,4,6,-8], 5))
print(insert_shift_array([42,8,15,23,42], 16))
print(insert_shift_array([], 7))
