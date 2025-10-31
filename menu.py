menu_item = ["bergur" , "pizza" , "pasta" , "kfc"]
price = [3.99,4.99,5.99,2.99]

for item,price in zip(menu_item,price):
    print (f"{item:<10}  {price:>6.2f}$")