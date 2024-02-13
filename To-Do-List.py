print("Hey, Welcome! This is a TO-DO-LIST.")
tasks = []

while True:
    task_input = input("Enter your list item (Type 'q' to quit): ").strip()

    if task_input.lower() == 'q':
        break

    if task_input:
        tasks.append(task_input)
    else:
        print("Invalid input! Task cannot be empty. Please try again.")

print("\nYour TO-DO list:")
for idx, task in enumerate(tasks, start=1):
    print(f"{idx}. {task}")

print("Thank you for using the TO-DO list!")
