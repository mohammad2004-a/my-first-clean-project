# def even_numbers_list(n):
#     result = []
#     for i in range(n):
#         if i % 2 == 0:
#             result.append(i)
#     return result

# my_list = even_numbers_list(100)
# print(my_list)


def even_numbers_gen(n):
    print("Generator starting...")
    for i in range(n):
        if i % 2 == 0:
            yield i


my_gen = even_numbers_gen(80)
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
