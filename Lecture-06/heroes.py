heroes = ['Ironman', 'Thor', 'Hulk', 'Spiderman']

def display_heroes():
    print("\nHeroes list:")
    for hero in heroes:
        print("-", hero)

def add_hero():
    name = input("Enter hero name to add: ")
    heroes.append(name)
    print(name, "added.")

def insert_hero():
    name = input("Enter hero name to insert: ")
    index = int(input("Enter position (0 = first): "))
    if 0 <= index <= len(heroes):
        heroes.insert(index, name)
        print(name, "inserted at position", index)
    else:
        print("Invalid position.")

def remove_hero():
    name = input("Enter hero name to remove: ")
    if name in heroes:
        heroes.remove(name)
        print(name, "removed.")
    else:
        print(name, "not found in list.")

def sort_heroes():
    order = input("Enter order (asc/desc): ").lower()
    if order == "asc":
        sorted_list = sorted(heroes)
    elif order == "desc":
        sorted_list = sorted(heroes, reverse=True)
    else:
        print("Invalid order.")
        return
    print("\nSorted Heroes:")
    for hero in sorted_list:
        print("-", hero)

while True:
    print("\n--- HERO MENU ---")
    print("1. Display Heroes")
    print("2. Add Hero")
    print("3. Insert Hero")
    print("4. Remove Hero")
    print("5. Display Sorted Heroes")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        display_heroes()
    elif choice == '2':
        add_hero()
    elif choice == '3':
        insert_hero()
    elif choice == '4':
        remove_hero()
    elif choice == '5':
        sort_heroes()
    elif choice == '6':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
