tasks = []

while True:
    print("\n--- TO DO LIST ---")
    print("1 - Add task")
    print("2 - Show tasks")
    print("3 - Remove task")
    print("4 - Exit")

    choice = input("Choose: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "2":
        print("Your tasks:")
        for i, t in enumerate(tasks):
            print(i + 1, t)

    elif choice == "3":
        num = int(input("Enter task number to remove: "))
        if 0 < num <= len(tasks):
            tasks.pop(num - 1)
            print("Task removed!")
        else:
            print("Invalid number")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")