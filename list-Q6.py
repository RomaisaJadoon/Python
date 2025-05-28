shoppinglist = ["milk", "bread", "eggs", "butter", "juice",  

                 "sugar", "salt", "biscuits", "tea", "coffee"] 

 
# displaying items using loop
print("Here is your current shopping list:") 
for item in shoppinglist: 
    print("- " + item) 

# addition of item by user if needed
additem = input("\nDo you want to add an item to the list? (yes/no): ") 

if additem == "yes": 
    newitem = input("Enter the item you want to add: ")
    shoppinglist.append(newitem) 
    print(f"'{newitem}' has been added to the list.") 

# removal of item by user 
removeitem = input("\nDo you want to remove an item from the list? (yes/no): ")

if removeitem == "yes": 
    itemtoremove = input("Enter the item you want to remove: ")
    if itemtoremove in shoppinglist: 
        shoppinglist.remove(itemtoremove) 
        print(f"'{itemtoremove}' has been removed from the list.") 

    else: 
        print("Item not found in the list.") 

# displaying of final list
print("\nHere is your updated shopping list:") 
for item in shoppinglist: 
    print("- " + item) 