#Shopping list

shopping_list = []

while True:
    item = input("Enter an item (or done to finish): ")
    if item.lower() == "done":
        break
    shopping_list.append(item)

print("Your shopping list:", shopping_list)