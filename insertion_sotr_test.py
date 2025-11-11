from incertion_sort import insertion_sort


def test_insertion_sort():
    assert insertion_sort([9, 8, 4, 6, 2, 3, 1]) == [1, 2, 3, 4, 6, 8, 9]
    assert insertion_sort([1, 1, 1, 1]) == [1, 1, 1, 1]
    assert insertion_sort([]) == []
    assert insertion_sort(["s", "a", "w"]) == []
    assert insertion_sort([1, 8, 5, 1, 3, "k", 4, 7, "s", "d"]) == [1, 1, 3, 4, 5, 7, 8]
