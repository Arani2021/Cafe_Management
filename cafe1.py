menu = {
    'Pizza': 100,
    'Pasta': 130,
    'Salad': 70,
    'Coffee': 80,
}

print("Welcome to the Dasgupta cafe")
print("Pizza: Rs 100\nPasta: Rs 130\nSalad: Rs 70\nCoffee: Rs 80")

order_total = 0

for i in range(4):
    item = input("Enter the name of the item (or type 'done' to finish ordering): ")
    if item.lower() == "done":
        break
    elif item.capitalize() in menu:
        order_total += menu[item.capitalize()]
        print(f"Your item {item} has been added to your order.")
    else:
        print(f"Sorry, {item} is not available on the menu.")
if order_total > 120:
    discount = 0.15 * order_total
    order_total -= discount
    print("Congratulations! You qualify for a 15% discount.")
print(f"The total amount of the items is Rs {order_total}")

