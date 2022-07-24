import pytest
from Sorting.insertion.insertion import insertion_sort


@pytest.mark.parametrize(
    "test_arr,expected",
    [
        ([8, 4, 23, 42, 16, 15], [4, 8, 15, 16, 23, 42]),
        ([20, 18, 12, 8, 5, -2], [-2, 5, 8, 12, 18, 20]),
        ([5, 12, 7, 5, 5, 7], [5, 5, 5, 7, 7, 12]),
        ([2, 3, 5, 7, 13, 11], [2, 3, 5, 7, 11, 13]),
    ],
)
def test_all_cases(test_arr, expected):
    insertion_sort(test_arr)
    assert test_arr == expected
