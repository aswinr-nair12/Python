grocery_list = ["milk", "bread", "eggs"]
print("Initial Grocery List:", grocery_list)

def add_item(item):
    grocery_list.append(item)
    print("After adding item:", grocery_list)

add_item("butter")

def remove_last_item():
    if grocery_list:
        removed = grocery_list.pop()
        print("After removing last item:", grocery_list)

remove_last_item()

display_items = lambda items: [print("Item:", item) for item in items]

print("Displaying Grocery Items:")
display_items(grocery_list)

def count_characters(items):
    if not items:          
        return 0
    return len(items[0]) + count_characters(items[1:])

total_characters = count_characters(grocery_list)
print("Total number of characters:", total_characters)


