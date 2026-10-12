
# Part B - Shopping List Manager

shopping_list = []

while True:
    print("\n--- Shopping List Menu ---")
    print("add / remove / show / done")

    choice = input("Choose an action: ").strip().lower()

    if choice == "add":
        item = input("Enter the item to add: ").strip()

        if item:
            shopping_list.append(item)
            print(f"{item} has been added to your list.")
        else:
            print("Item cannot be empty.")

    elif choice == "remove":
        item = input("Enter the item to remove: ").strip()

        if item in shopping_list:
            shopping_list.remove(item)
            print(f"{item} has been removed from your list.")
        else:
            print("That item is not on your list.")

    elif choice == "show":
        print("\nYour shopping list:")

        if shopping_list:
            for item in shopping_list:
                print(item)
        else:
            print("Your list is empty.")

    elif choice == "done":
        print("Goodbye! Happy shopping!")
        break

    else:
        print("Invalid choice. Please enter add, remove, show, or done.")
