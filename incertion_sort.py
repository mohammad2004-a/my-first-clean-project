import logging

logging.basicConfig(
    filename="log.insertion_sort.log",
    level=logging.DEBUG,
    filemode="a",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)


logging.info("start the insertion sort method ")


def insertion_sort(unsorted):
    """Return a sorted version of a list."""
    logging.debug("The function received a list.")
    sorted = []
    for new_item in unsorted:
        i = 0
        for sorted_item in sorted:
            if new_item >= sorted_item:
                i += 1
            else:
                break
        sorted.insert(i, new_item)
        logging.debug("The function is sorting the list.")
    logging.debug("the list is sorted")
    return sorted


logging.info("the insertion sort method ended")

assert insertion_sort([9, 8, 4, 6, 2, 3, 1]) == [1, 2, 3, 4, 6, 8, 9]
assert insertion_sort([1, 1, 1, 1]) == [1, 1, 1, 1]
assert insertion_sort([]) == []
