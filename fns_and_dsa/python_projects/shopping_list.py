def user_menu():
   print("sports cars Shopping List Manager")
   print("1. Add Item")
   print("2. Remove Item")
   print("3. View List")
   print("4. Exit")

def add_item (shopping_list):
   item = input("Enter the item you want to add: \n")
   shopping_list.append(item)
   print(f"you add '{item}' to the list ")

def remove_item (shopping_list):
   item = str(input("Enter the item you want to remove : \n"))
   if item in shopping_list:
      shopping_list.remove(item)
      print(f"you remove {item} from the list")
   else:
    print(f"Item '{item}' is not in the list.")

def view_list (shopping_list):
   
   if shopping_list :
      print("current shopping list: ")
      items_with_index = [f"{index}: {item}" for index, item in enumerate(shopping_list, start=1)] # Use a repeat list to group items with space between them
      print(" - ".join(items_with_index))   # join => give space betwin them
   else :
      print("your shopping list is empty")
def main():
   shopping_list = [ "Ferrari 488 GTB", "Lamborghini Huracan", "Chevrolet Corvette" , ]
   while True:
     user_menu()
     choice = input("Enter your choice: \n")
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
