import logging

logging.basicConfig(
    filename="log.insertion_sort.log",
    level=logging.DEBUG,
    filemode="a",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)


def insertion_sort(unsorted):
    """Return a sorted version of a list."""
    logging.info("start the insertion sort method ")
    logging.debug("The function received a list.")

    item_to_sort = []
    invalid_item = []
    result_sort = []

    logging.debug("List filter started")
    for item in unsorted:
        try:
            valid_item = float(item)
            item_to_sort.append(valid_item)
        except ValueError:
            logging.error("You cannot enter a string.")
            invalid_item.append(item)
        except TypeError:
            logging.error("The entered value is not valid.")
            invalid_item.append(item)
    logging.debug("list filter ended")
    if invalid_item:
        logging.warning(f"The program cannot sort these values: {invalid_item}")
    if item_to_sort:
        logging.debug("The function is sorting the list.")
        for new_item in item_to_sort:
            i = 0
            for sorted_item in result_sort:
                if new_item >= sorted_item:
                    i += 1
                else:
                    break
            result_sort.insert(i, new_item)
        logging.debug("the list is sorted")
    else:
        logging.warning("None of the values ​​in the list were numbers.")
    logging.info("the insertion sort method ended")
    return result_sort


# assert insertion_sort([9,8,4,6,2,3,1]) == [1,2,3,4,6,8,9]
# assert insertion_sort([1,1,1,1]) == [1,1,1,1]
# assert insertion_sort([]) == []
# assert insertion_sort(["salam" , 32 , 74 , 12 , "KHODAHAFEZ"])==({12,32,74])

print(insertion_sort([[9, 8, 4, "salam", 2, 3, 1]]))
