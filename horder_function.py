import logging

logging.basicConfig(
    filename="horder_function.log",
    filemode="w",
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)


def my_decorator(x):
    def wrapper():
        logging.info("the function started")
        print(f"the {x.__name__} is runnig : x * y = {x(4,5)}")
        logging.info("the function ended")

    return wrapper


@my_decorator
def my_function(x: int, y: int) -> int:
    return x * y


my_function()
