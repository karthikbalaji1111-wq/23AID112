#creating empty list
shopping = []

while True:
    choice = input("What would you like to do? (add, remove, show, or quit: )")

    #add item
    if option == "add":
        item = input("Enter item: ")
        shopping.append(item)
    
    #remove item
    elif option == "remove":
        item = input("Enter item to remove: ")
        if item in shopping_list:
            shopping.remove(item)
        else:
            print("item not in list")

    #show items 
    elif option == "show":
        print("Your shopping list:", shopping)

    elif option == "quit":
        break

    else:
        print("Invalid option input")
print("Final shopping list:", shopping)
