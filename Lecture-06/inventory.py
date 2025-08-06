def update_inventory(inventory, item_name, quantity_sold):
    for item in inventory:
        if item[0] == item_name:
            item[1] -= quantity_sold
            break

def calculate_total_value(inventory):
    total = 0
    for item in inventory:
        quantity = item[1]
        price = item[2]
        total += quantity * price
    return total

def find_most_expensive(inventory):
    most_expensive = inventory[0]
    for item in inventory:
        if item[2] > most_expensive[2]:
            most_expensive = item
    return most_expensive[0]

def add_item(inventory, item_name, quantity, price):
    for item in inventory:
        if item[0] == item_name:
            item[1] = quantity
            item[2] = price
            return
    inventory.append([item_name, quantity, price])

inventory = [
    ["Apple", 50, 0.75],
    ["Banana", 100, 0.50],
    ["Orange", 75, 0.80]
]

update_inventory(inventory, "Banana", 20)

total = calculate_total_value(inventory)
print("Total value of inventory: $", total)

expensive_item = find_most_expensive(inventory)
print("Most expensive item:", expensive_item)

add_item(inventory, "Eggs", 30, 0.25)
add_item(inventory, "Eggs", 50, 0.30)

print("\nFinal inventory:")
for item in inventory:
    print(item)
