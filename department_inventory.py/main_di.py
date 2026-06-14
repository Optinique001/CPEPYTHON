# Department Inventory System

items = [
    [1, "Arduino Uno", "Available"],
    [2, "Multimeter", "Available"],
    [3, "Oscilloscope", "Borrowed"]
]


# View Available Items
def view_available():
    available_items = [item for item in items if item[2] == "Available"]

    if available_items:
        print("\nAvailable Items:")
        for item in available_items:
            print(f"{item[0]}. {item[1]}")
    else:
        print("\nNo items available.")


# Borrow Item
def borrow_item(item_name):
    for item in items:
        if item[1].lower() == item_name.lower():
            if item[2] == "Available":
                item[2] = "Borrowed"
                print(f"\n{item_name} borrowed successfully.")
            else:
                print(f"\n{item_name} is already borrowed.")
            return

    print("\nItem not found.")


# Return Item
def return_item(item_name):
    for item in items:
        if item[1].lower() == item_name.lower():
            if item[2] == "Borrowed":
                item[2] = "Available"
                print(f"\n{item_name} returned successfully.")
            else:
                print(f"\n{item_name} is already available.")
            return

    print("\nItem not found.")


# Add New Item
def add_new_item(item_name):
    item_id = len(items) + 1
    items.append([item_id, item_name, "Available"])
    print(f"\n{item_name} added successfully.")


# Main Menu
while True:
    print("\n===== DEPARTMENT INVENTORY =====")
    print("1. View Available Items")
    print("2. Borrow Item")
    print("3. Return Item")
    print("4. Add New Item")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        view_available()

    elif choice == "2":
        name = input("Enter item name: ")
        borrow_item(name)

    elif choice == "3":
        name = input("Enter item name: ")
        return_item(name)

    elif choice == "4":
        name = input("Enter new item name: ")
        add_new_item(name)

    elif choice == "5":
        print("\nExiting program...")
        break

    else:
        print("\nInvalid choice.")