
lst=[]

while True:
    print("Menu:")
    print("1. Add a number to the list")
    print("2. Remove a number from the list")
    print("3. Insert a number at a specific position")
    print("4. Pop a number from the list")
    print("5. Find the sum, average, and maximum of the list")
    print("6. Search for a number in the list")
    print("7. Remove all odd numbers from the list")
    print("8. Exit")

    choice = input("Enter your choice: ")
    choice = int(choice)
    if choice == 1:
        num_input = input("Enter a number to add: ")
        lst.append(num_input)
        print("Number added to the list.")
        
    elif choice == 2:
        num_input = input("Enter a number to remove: ")
        if num_input.replace('.', '', 1):
            num = float(num_input)
            if num in lst:
                lst.remove(num)
                print("Number removed from the list.")
            else:
                print("Number not found in the list.")
        else:
            print("Invalid input! Please enter a valid number.")
        
    elif choice == 3:
        num_input = input("Enter a number to insert: ")
        if num_input.replace('.', '', 1):
            num = float(num_input)
            index_input = input("Enter the index to insert the number at: ")
            index = int(index_input)
            if 0 <= index <= len(lst):
                lst.insert(index, num)
                print("Number inserted at position", index)
            else:
                print("Invalid input! Please enter a valid index.")
        else:
            print("Invalid input! Please enter a valid number.")
        
    elif choice == 4:
        index_input = input("Enter the index to pop: ")
        index = int(index_input)
        if 0 <= index < len(lst):
            popped_value = lst.pop(index)
            print(f"Number popped from the list: {popped_value}")
        else:
            print("Invalid input! Please enter a valid index.")
        
    elif choice == 5:
        if lst:
            total = int(sum(lst))
            avg = int(total / len(lst))
            max_val = int(max(lst))
            print("Sum: ",total,", Average: ",avg,", and Maximum: ",max_val)
        else:
            print("The list is empty.")
        
    elif choice == 6:
        num_input = input("Enter a number to search for: ")
        if num_input.replace('.', '', 1):
            num = float(num_input)
            if num in lst:
                print(f"Number found at index {lst.index(num)}.")
            else:
                print("Number not found in the list.")
        else:
            print("Invalid input! Please enter a valid number.")
        
    elif choice == 7:
        lst[:] = [num for num in lst if num % 2 == 0]
        print("All odd numbers removed from the list.")
        
    elif choice == 8:
        print("Thank you for using the List Operations Program. Goodbye!")
        break
        
else:
    print("Invalid choice, please try again.")

        
    if lst:
        print("Current list:", lst)
    else:
        print("The list is currently empty.")
        
        show_list = input("Would you like to print the current list? (yes/no): ").lower()
        if show_list == "yes":
            if lst:
                print("Current list:", lst)
            else:
                print("The list is currently empty.")

        else:
            print("Invalid input! Please enter a valid option.")