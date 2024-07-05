def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def add_item(shopping_list):
    item = input("Enter the item you want to add: ")
    shopping_list.append(item)
    print(f"Item '{item}' added to the list.")

def remove_item(shopping_list):
    item = input("Enter the item you want to remove: ")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"Item '{item}' removed from the list.")
    else:
        print(f"Item '{item}' is not in the list.")

def view_list(shopping_list):
    if shopping_list:
        print("Current Shopping List:")
        for index, item in enumerate(shopping_list, start=1):
            print(f"{index}. {item}")
    else:
        print("Your shopping list is empty.")

def main():
    shopping_list = ["Porsche 911", "Ferrari 488 GTB", "Lamborghini Huracan",
                     "Chevrolet Corvette", "BMW M4", "Mercedes-AMG GT", "Ford Mustang"]

    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_item(shopping_list)
        elif choice == '2':
            remove_item(shopping_list)
        elif choice == '3':
            view_list(shopping_list)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
