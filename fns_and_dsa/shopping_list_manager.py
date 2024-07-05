def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def add_item(shopping_list):
    item = input("\nEnter the item you want to add: ")
    shopping_list.append(item)
    print(f"'{item}' has been added to the list.")

def remove_item(shopping_list):
    item = input("\nEnter the item you want to remove: ")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"'{item}' has been removed from the list.")
    else:
        print(f"'{item}' is not found in the list.")

def view_list(shopping_list):
    if shopping_list:
        print("\nCurrent Shopping List:")
        for index, item in enumerate(shopping_list, start=1):
            print(f"{index}. {item}")
    else:
        print("\nThe shopping list is empty.")

def main():
    shopping_list = []  

    while True:
        display_menu()  

        try:
            choice = int(input("\nEnter your choice: "))  
        except ValueError:
            print("\nInvalid input. Please enter a number.")
            continue

        if choice == 1:
            add_item(shopping_list)
        elif choice == 2:
            remove_item(shopping_list)
        elif choice == 3:
            view_list(shopping_list)
        elif choice == 4:
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid choice. Please enter a valid option (1-4).")

if __name__ == "__main__":
    main()
