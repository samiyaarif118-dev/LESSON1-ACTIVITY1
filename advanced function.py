items =["pencil", "eraser", "ruler", "pen", "glue"]
stock_count = [5, 34, 15, 17, 0]
inventory = {
    item:count for item, count in zip(items, stock_count)
}
print("inventory: ", inventory)

in_stock_item = [item for item in items if inventory[item] > 0]
print("stock item : ", in_stock_item)

choosen_item = input("Enter your item: ")
if choosen_item not in inventory or inventory[choosen_item] == 0:
    print("Item is out of stock")
    exit()

prices =[5, 6, 2, 8, 7]
markup = int(input("Enter your price"))
new_prices = list(map(lambda x: x + markup, prices))
print("new prices: ", new_prices)

inventory [choosen_item] = inventory[choosen_item] -1
print("updated inventory: ", inventory)

print("item bought: ", choosen_item)
print("price payed: ",new_prices[items.index(choosen_item)])





