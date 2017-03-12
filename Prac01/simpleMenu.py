MENU = "(H)ello\n(G)oodbye\n(Q)uit"
name = str(input("Enter name: "))
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "H":
        print("Hello " + name)
    elif choice == "G":
        print("Goodbye " + name)
    else:
        print("Invalid choice.")
    print(MENU)
    choice = input(">>> ").upper()
print("Finished.")

test test