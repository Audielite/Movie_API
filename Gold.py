# make a list that holds our items
shopping_list = []

print("What should we get from the store?")

def show_help():
# print out instructions on how to use the app
    print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' to get instructions.
Enter 'SHOW' to see your current list.
""")

def show_list():
# print out list
    print("Here's your list:")

    for item in shopping_list:
        print(item)

def add_to_list(new_item):
# addnew items to our list
    shopping_list.append(new_item)
    print("Added {}. List now has {} items.".format(new_item, len(shopping_list)))

show_help()

while True:
# ask for new items
    new_item = input("> ")
# be able to quit the app
    if new_item == 'DONE':
        break
    elif new_item == 'HELP':
        show_help()
        continue
    elif new_item == 'SHOW':
        show_list()
        continue
    add_to_list(new_item)

show_list()
