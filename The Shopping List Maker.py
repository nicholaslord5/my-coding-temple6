# Objective: The aim of this assignment is to create a program that helps users make a shopping list.

# Task 1: Write a function that lets the user add items to a list.

# Task 2: Include a function to remove items from the list.

# Task 3: Add a function that prints out the entire list in a formatted way.

shopping_list = [] ### Task 1 ###

def add_item(item): ### Task 2 ###
    shopping_list.append(item)
    print(f"{item} added to shopping list.")

def remove_item(item): ### Task 2 ###
    shopping_list.remove(item)
    print(f"{item} removed from list.")

def print_list(): ### Task 4 ###
    if shopping_list:
        print("\nShopping List:")
        for index, item in enumerate(shopping_list, start=1):
            print(f"{index}. {item}")

### was going to stop here, but there was no output, so here's some more ###
def main():
    while True:
        print("\nSelect option:")
        print("1. Add item")
        print("2. Remove item")
        print("3. Show shopping list")
        print("4. Quit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            item = input("Which item would you like to add? ")
            add_item(item)
        elif choice == '2':
            item = input("Which item would you like to remove? ")
            remove_item(item)
        elif choice == '3':
            print_list()
        elif choice == '4':
            print("So long and happy shopping!")
            break
        else:
            print("Invalid choice. Please input a number from the list.")

if __name__ == "__main__":
    main()