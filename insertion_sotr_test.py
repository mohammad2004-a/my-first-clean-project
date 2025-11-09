from incertion_sort import insertion_sort


def test_insertion_sort():
    assert insertion_sort([9, 8, 4, 6, 2, 3, 1]) == [1, 2, 3, 4, 6, 8, 9]
    assert insertion_sort([1, 1, 1, 1]) == [1, 1, 1, 1]
    assert insertion_sort([]) == []
