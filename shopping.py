#shopping list manager
#You are asked to create a shopping list manager. 
#The user can add items to shopping list when "done" is typed, the input system closes and you need to display the list along with the total number of items
items = []

print("Enter items. Type 'done' to finish:")

while True:
    new_item = input("enter item:")

    if new_item.lower() == "done":
        break
    else:
        items.append(new_item)

print("Your items are:")
for item in items:
    print(item)

    