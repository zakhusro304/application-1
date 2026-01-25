def main():
    buffer = ""  # input buffer

    while True:
        print("\nText Menu")
        print("1. Append data to the input buffer")
        print("2. Clear the input buffer")
        print("3. Display the input buffer")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            new_data = input("Enter text to append: ")
            buffer += new_data
            print("Data appended.")

        elif choice == "2":
            buffer = ""
            print("Input buffer cleared.")

        elif choice == "3":
            print("Current input buffer:")
            print(buffer if buffer else "(buffer is empty)")

        elif choice == "4":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()

