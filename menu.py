# menu_item = ["bergur" , "pizza" , "pasta" , "kfc"]
# price = [3.99,4.99,5.99,2.99]

# for item,price in zip(menu_item,price):
#     print (f"{item:<10}  {price:>6.2f}$")


# dict = {"ali": "f566", "reza": "f4845", "javad": "g656560"}

# n_dict = {name: value[:2] for name, value in dict.items()}
# print(n_dict)

data = [(1, 5), (3, 2), (2, 8)]
sorted_data = sorted(data, key=lambda item: item[0])
print(sorted_data)
