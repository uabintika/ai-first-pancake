# Each person has name, age, and city
# The application will you to add a person to a list (in memory)
# and after addition, it will print the list of people
task_list = []

while True:

    task_name = input("Enter task name: ")
    task_description = input("Enter task description: ")
    task_due_date = input("Enter task due date: ")
    task_priority = input("Enter task priority: ")

    try:
        year, month, day = task_due_date.strip().split()
        formatted_date = f"{year}.{month}.{day}"
    except ValueError:
        print("Invalid date format. Please enter the date in YYYY MM DD format.")
        continue

    task = {
        'name': task_name,
        'description': task_description,
        'due_date': formatted_date,
        'priority': task_priority
    }
    task_list.append(task)
    for t in task_list:
        print(f"Name: {t['name']}, Description: {t['description']}, Due Date: {t['due_date']}, Priority: {t['priority']}")  
