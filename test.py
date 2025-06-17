print("What would you like to do?")
print("1. Add new entry")
print("2. View all entries")
print("3. Exit")

choice = input("Enter your choice: ")

if choice == "1":
    print("You chose to add an entry.")
elif choice == "2":
    print("You chose to view entries.")
elif choice == "3":
    print("Exiting...")
    exit()
else:
    print("Invalid choice.")
