#list  supermarket items
supermarket_items = ["apples", "bananas", "carrots", "dates", "eggs"]
# print("Supermarket Items:")
# for item in supermarket_items:
#     print(item) 

#     #list slicing
# print("\nSliced Items (index 1 to 3):")
# sliced_items = supermarket_items[1:4]
# for item in sliced_items:
#     print(item)

#     #list indexing
# print("\nItem at index 2:")
# print(supermarket_items[3]) 

# #list len()
# print("\nTotal number of items in the supermarket list:")
# print(len(supermarket_items))

# #list append()
# print("\nAdding 'flour' to the supermarket items list.")
# supermarket_items.append("flour")
# print("Updated Supermarket Items:")
# for item in supermarket_items:
#     print(item) 

# #list remove()
# print("\nRemoving 'carrots' from the supermarket items list.")
# supermarket_items.remove("carrots")
# print("Updated Supermarket Items:")
# for item in supermarket_items:
#     print(item)

# #list extend()
# print("\nExtending supermarket items with ['grapes', 'honey'].")
# supermarket_items.extend(["grapes", "honey"])
# print("Updated Supermarket Items:")
# for item in supermarket_items:
#     print(item)

# #list insert()
# print("\nInserting 'bread' at index 2.")
# supermarket_items.insert(2, "bread")
# print("Updated Supermarket Items:")
# for item in supermarket_items:
#     print(item)

#list pop()
print("\nPopping the last item from the supermarket items list.")
popped_item = supermarket_items.pop()
print(f"Popped Item: {popped_item}")
print("Updated Supermarket Items:")
for item in supermarket_items:
    print(item) 

#list clear()  
print("\nClearing all items from the supermarket items list.")
supermarket_items.clear()
print("Supermarket Items after clearing:")
print(supermarket_items)  # Should print an empty list

#list split()
print("\nSplitting a string of items into a list.")
items_string = "milk,cheese,butter,yogurt"
items_list = items_string.split(",")
print("Items List:")
for item in items_list:
    print(item)
    print(type(item)) # list convert string 

#list join()
print("\nJoining a list of items into a single string.")
joined_string = ", ".join(items_list)
print("Joined String:")
print(joined_string)
print(type(joined_string)) # string convert list